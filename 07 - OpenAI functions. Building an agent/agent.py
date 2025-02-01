import os
import pandas as pd
import streamlit as st
import logging
from dotenv import load_dotenv
from openai import OpenAI

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Constants
DATASET_PATH = "heart_attack_youngsters_india.csv"

# Streamlit UI
st.title("Agent AI Assistant: Dataset Analyzer")

# Load dataset
@st.cache_data
def load_data(dataset_path):
    """Load the dataset from the specified path."""
    try:
        data = pd.read_csv(dataset_path)
        logging.info(f"Dataset loaded successfully from {dataset_path}")
        return data
    except FileNotFoundError:
        logging.error(f"Dataset file not found at path: {dataset_path}")
        st.error(f"Dataset file not found: {dataset_path}")
        return None
    except Exception as e:
        logging.error(f"Error loading dataset: {e}")
        st.error(f"Error loading dataset: {e}")
        return None

# Analyze dataset dynamically based on user query
def analyze_dataset(data, question):
    """
    Analyze the dataset and extract relevant insights based on the user's question.

    :param data: The dataset as a pandas DataFrame.
    :param question: The user's question.
    :return: Dictionary of relevant insights.
    """
    try:
        total_count = len(data)
        high_risk_count = len(data[data["Heart Attack Likelihood"] == "Yes"])
        high_risk_percentage = (high_risk_count / total_count) * 100 if total_count > 0 else 0

        # Store general insights
        insights = {
            "total_individuals": total_count,
            "high_risk_percentage": round(high_risk_percentage, 2),
        }

        # Extract statistics based on user question
        if "age" in question.lower():
            if "average" in question.lower():
                insights["average_age_high_risk"] = round(data[data["Heart Attack Likelihood"] == "Yes"]["Age"].mean(), 2)
            elif "group" in question.lower():
                insights["age_distribution"] = data["Age"].value_counts().to_dict()

        if "gender" in question.lower():
            insights["risk_by_gender"] = data.groupby("Gender")["Heart Attack Likelihood"].apply(lambda x: round((x == "Yes").mean() * 100, 2)).to_dict()

        if "smoking" in question.lower():
            insights["risk_by_smoking_status"] = data.groupby("Smoking Status")["Heart Attack Likelihood"].apply(lambda x: round((x == "Yes").mean() * 100, 2)).to_dict()

        if "alcohol" in question.lower():
            insights["risk_by_alcohol_consumption"] = data.groupby("Alcohol Consumption")["Heart Attack Likelihood"].apply(lambda x: round((x == "Yes").mean() * 100, 2)).to_dict()

        if "bmi" in question.lower() or "weight" in question.lower():
            insights["bmi_impact"] = data.groupby(pd.cut(data["BMI (kg/m²)"], bins=[0, 18.5, 25, 30, 35, 40, 100], labels=["Underweight", "Normal", "Overweight", "Obese", "Severely Obese", "Morbidly Obese"]))["Heart Attack Likelihood"].apply(lambda x: round((x == "Yes").mean() * 100, 2)).to_dict()

        if "diabetes" in question.lower():
            insights["risk_by_diabetes"] = data.groupby("Diabetes")["Heart Attack Likelihood"].apply(lambda x: round((x == "Yes").mean() * 100, 2)).to_dict()

        if "hypertension" in question.lower():
            insights["risk_by_hypertension"] = data.groupby("Hypertension")["Heart Attack Likelihood"].apply(lambda x: round((x == "Yes").mean() * 100, 2)).to_dict()

        return insights

    except Exception as e:
        logging.error(f"Error analyzing dataset: {e}")
        return {"error": "Unable to analyze dataset", "details": str(e)}

# Generate response with OpenAI API
def generate_response(prompt, analysis_results):
    """
    Generate a natural language response using OpenAI's GPT model.

    :param prompt: The user's query.
    :param analysis_results: The extracted insights.
    :return: A natural language response.
    """
    try:
        # Format insights for the prompt
        formatted_results = "\n".join([f"{key}: {value}" for key, value in analysis_results.items()])

        # Create concise context
        context = f"""
        You are a data analysis assistant. Below are the relevant insights from the dataset:

        {formatted_results}

        Based on this, answer the following question concisely and accurately:
        {prompt}
        """

        # Call OpenAI API with optimized input
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": context},
            ],
        )

        return response.choices[0].message.content

    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response. Please try again."

# Main function
def main():
    """Main function to run the Agent AI Assistant."""
    # Load dataset
    data = load_data(DATASET_PATH)
    if data is None:
        return

    # Display dataset preview
    st.write("### Dataset Preview")
    st.write(data.head())

    # User input for query
    st.write("### Ask a Question")
    user_query = st.text_input("Enter your question about the dataset:", "")

    # Analyze dataset and generate response
    if st.button("Get Answer"):
        if not user_query:
            st.warning("Please enter a question.")
        else:
            # Perform dataset analysis dynamically based on the query
            analysis_results = analyze_dataset(data, user_query)

            # Generate natural language response
            response = generate_response(user_query, analysis_results)

            # Display the response
            st.write("### Agent AI Assistant Response:")
            st.write(response)

# Run the app
if __name__ == "__main__":
    main()
