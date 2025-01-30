import os
import requests
import sqlite3
from tenacity import retry, wait_random_exponential, stop_after_attempt
from dotenv import load_dotenv
from conversation import Conversation
import pandas as pd
import streamlit as st
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  
MODEL = "gpt-3.5-turbo"
DATABASE = "heart_attack_data.sqlite"
DATASET_PATH = "heart_attack_youngsters_india.csv"


# Database schema string
database_schema_string = """
Table: health_data
Columns: Age, Gender, Region, Urban/Rural, SES, Smoking Status, Alcohol Consumption, 
          Diet Type, Physical Activity Level, Screen Time (hrs/day), Sleep Duration (hrs/day), 
          Family History of Heart Disease, Diabetes, Hypertension, Cholesterol Levels (mg/dL), 
          BMI (kg/m²), Stress Level, Blood Pressure (systolic/diastolic mmHg), 
          Resting Heart Rate (bpm), ECG Results, Chest Pain Type, Maximum Heart Rate Achieved, 
          Exercise Induced Angina, Blood Oxygen Levels (SpO2%), Triglyceride Levels (mg/dL), 
          Heart Attack Likelihood
"""
print(f"Database schema string: '{database_schema_string}'")
functions = [
    {
        "name": "ask_database",
        "description": "Query the health database with flexible SQL conditions",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": """
                    SQL query to extract health data. 
                    Supports filtering by Age, Stress, and other columns.
                    {database_schema_string}
                    The query should be returned in plain text, not in JSON
                    Example: 
                    - 'SELECT * FROM health_data WHERE Age > 40 AND Stress = "High"'
                    - 'SELECT Age, Stress FROM health_data WHERE Stress = "Medium"'
                    """
                }
            },
            "required": ["query"]
        }
    },
    {
         "name": "analyze_dataset",
        "description": "Use this function to analyze the dataset and return statistical insights.",
        "parameters": {
            "type": "object",
            "properties": {
                "filter_column": {
                    "type": "string",
                    "description": """Column name to filter dataset (e.g., 'Stress Level', 'Age', 'Gender').
                    {database_schema_string}"""
                },
                "filter_value": {
                    "type": "string",
                    "description": "Value of the filter column (e.g., 'High' for stress level, 'Male' for gender)."
                }
            },
            "required": []
        }
    }
]

@retry(wait=wait_random_exponential(min=1, max=40), stop=stop_after_attempt(3))
def chat_completion_request(messages, functions=None, model=MODEL):
    """Handles API request to OpenAI."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    json_data = {"model": model, "messages": messages}
    if functions:
        json_data["functions"] = functions

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )
        response_json = response.json()
        logging.info(f"OpenAI API Response: {response_json}")
        return response_json
    except Exception as e:
        logging.error(f"Unable to generate response: {e}")
        return {"choices": [{"message": {"content": f"Error: {e}"}}]}


def chat_completion_with_function_execution(messages, functions=None):
    try:
        response_json = chat_completion_request(messages, functions)

        if "error" in response_json:
            logging.error(f"API returned an error: {response_json['error']}")
            return {"choices": [{"message": {"content": f"API Error: {response_json['error']}"}}]}

        if "choices" in response_json and response_json["choices"]:
            choice = response_json["choices"][0]
            
            # Handle function calls
            if "function_call" in choice["message"]:
                function_name = choice["message"]["function_call"]["name"]
                function_args = eval(choice["message"]["function_call"]["arguments"]) if choice["message"]["function_call"]["arguments"] else {}

                if function_name == "ask_database":
                    query = function_args["query"]
                    logging.info(f"Executing database query: {query}")

                    # Execute the SQL query
                    results = ask_database(conn, query)

                    # Add function result back to messages
                    messages.append({
                        "role": "function", 
                        "name": function_name, 
                        "content": str(results)
                    })

                    # Get a new response with function results
                    return chat_completion_request(messages)
                
                elif function_name == "analyze_dataset":
                    logging.info("Analyzing dataset")
                    # Call analyze_dataset with the correct path
                    results = analyze_dataset(DATASET_PATH)
                    
                    # Prepare a human-readable response
                    if results:
                        content = (
                            f"Dataset Analysis:\n"
                            f"Total Individuals: {results['total_individuals']}\n"
                            f"High-Risk Individuals: {results['high_risk_individuals']}\n"
                            f"High-Risk Percentage: {results['high_risk_percentage']:.2f}%"
                        )
                    else:
                        content = "Unable to analyze dataset."

                    # Add function result back to messages
                    messages.append({
                        "role": "function", 
                        "name": function_name, 
                        "content": content
                    })

                    # Get a new response with function results
                    return chat_completion_request(messages)

            return response_json

        logging.error("Unexpected response format from OpenAI API.")
        return {"choices": [{"message": {"content": "Error: Unexpected API response format."}}]}

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return {"choices": [{"message": {"content": f"Error: {e}"}}]}



def ask_database(conn, query):
    try:
        logging.info(f"Executing SQL Query: {query}")  
        
        # Execute query and fetch results
        cursor = conn.cursor()
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        results = cursor.fetchall()
        
        # If query returns no results
        if not results:
            logging.warning("Query returned no results.")
            return "No matching data found. Please check your query or database records."
        
        # Format results as list of dictionaries
        formatted_results = [dict(zip(columns, row)) for row in results]
        
        # Prepare a human-readable summary
        summary = f"Found {len(results)} matching records:\n"
        for idx, record in enumerate(formatted_results[:5], 1):
            summary += f"{idx}. Age: {record.get('Age', 'N/A')}, Stress Level: {record.get('Stress Level', 'N/A')}, Region: {record.get('Region', 'N/A')}\n"
        
        if len(results) > 5:
            summary += f"... and {len(results) - 5} more records."
        
        return summary

    except sqlite3.OperationalError as e:
        logging.error(f"SQL Operational Error: {e}")
        return f"SQL Error: {e}. Please check your query syntax."
    
    except Exception as e:
        logging.error(f"Unexpected SQL Error: {e}")
        return f"Unexpected error: {e}"

def analyze_dataset(filter_column=None, filter_value=None, dataset_path=DATASET_PATH):
    """
    Provides flexible and dynamic dataset analysis
    
    :param filter_column: Column to filter the dataset
    :param filter_value: Value to filter the dataset
    :param dataset_path: Path to the CSV dataset
    :return: Dictionary of dataset insights
    """
    try:
        # Read the dataset
        data = pd.read_csv(dataset_path)
        
        # Apply filtering if specified
        if filter_column and filter_value:
            try:
                data = data[data[filter_column] == filter_value]
            except KeyError:
                logging.warning(f"Column {filter_column} not found in dataset")
                return {"error": f"Invalid column: {filter_column}"}
        
        # Comprehensive analysis with dynamic filtering
        total_count = len(data)
        high_risk_count = len(data[data["Heart Attack Likelihood"] == "Yes"])
        high_risk_percentage = (high_risk_count / total_count) * 100 if total_count > 0 else 0
        
        # More robust age group binning
        def categorize_age(age):
            if age < 25:
                return '18-24'
            elif 25 <= age < 35:
                return '25-34'
            elif 35 <= age < 45:
                return '35-44'
            elif 45 <= age < 55:
                return '45-54'
            elif 55 <= age < 65:
                return '55-64'
            else:
                return '65+'
        
        data['Age_Group'] = data['Age'].apply(categorize_age)
        
        # Dynamic analysis based on available data
        analysis_results = {
            "total_individuals": total_count,
            "high_risk_individuals": high_risk_count,
            "high_risk_percentage": round(high_risk_percentage, 2),
        }
        
        # Add analysis for categorical columns if they exist
        categorical_columns = [
            'Stress Level', 'Gender', 'Physical Activity Level', 
            'Age_Group', 'Diabetes', 'Hypertension'
        ]
        
        for column in categorical_columns:
            if column in data.columns:
                risk_by_category = data.groupby(column)['Heart Attack Likelihood'].apply(
                    lambda x: round((x == 'Yes').mean() * 100, 2)
                ).to_dict()
                analysis_results[f'risk_by_{column.lower().replace(" ", "_")}'] = risk_by_category
        
        # Logging for debugging
        logging.info("Dataset Analysis Results:")
        for key, value in analysis_results.items():
            logging.info(f"{key}: {value}")
        
        return analysis_results
    
    except Exception as e:
        logging.error(f"Comprehensive dataset analysis failed: {e}")
        return {
            "error": str(e),
            "message": "Unable to perform comprehensive dataset analysis"
        }

def call_function(messages, full_message):
    """Enhanced function call handling"""
    if full_message["message"]["function_call"]["name"] == "analyze_dataset":
        logging.info("Analyzing dataset")
        
        # Extract arguments safely
        try:
            function_args = eval(full_message["message"]["function_call"]["arguments"])
        except Exception:
            function_args = {}
        
        # Call analyze_dataset with extracted arguments
        results = analyze_dataset(
            filter_column=function_args.get('filter_column'),
            filter_value=function_args.get('filter_value')
        )
        
        # Convert results to a readable string
        content = "Dataset Analysis Results:\n"
        for key, value in results.items():
            content += f"{key}: {value}\n"
        
        messages.append({
            "role": "function",
            "name": "analyze_dataset",
            "content": content
        })
        
        return chat_completion_request(messages)
    
    return None
# Streamlit UI
if __name__ == "__main__":
    st.title("Agent AI Capstone Project")
    conn = sqlite3.connect(DATABASE)

    agent_system_message = """You are DatabaseGPT, a helpful assistant who gets answers to user questions from the Database
    or analyzes datasets to provide insights. Provide as many details as possible to your users. Begin!"""

    conversation = Conversation()
    conversation.add_message("system", agent_system_message)

    user_input = st.text_input("Ask a question about the data:", "")

    if user_input:
        conversation.add_message("user", user_input)

        chat_response = chat_completion_with_function_execution(conversation.conversation_history, functions=functions)

        assistant_message = chat_response.get("choices", [{}])[0].get("message", {}).get("content", "No response from assistant.")
        st.write("### Assistant Response:")
        st.write(assistant_message)

        conversation.add_message("assistant", assistant_message)

        with st.expander("Conversation History"):
            for message in conversation.conversation_history:
                st.write(f"**{message['role'].capitalize()}:** {message['content']}")
