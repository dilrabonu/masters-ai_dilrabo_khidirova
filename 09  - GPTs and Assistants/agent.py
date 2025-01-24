import os  # To access environment variables
import openai  # For OpenAI API interaction
import logging  # For logging purposes
from data_summarization_tool import DataSummarizationTool  # Summarization tool
from visualization_tool import VisualizationTool  # Visualization tool
import requests  # For making external API calls

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

class CapstoneAgent:
    def __init__(self, data_path='heart_attack_youngsters_india.csv'):
        """
        Initialize the Capstone Agent with tools and configuration.

        Args:
            data_path (str): Path to the dataset.
        """
        # Initialize data summarization tool
        self.data_tool = DataSummarizationTool(data_path)

        # Initialize visualization tool
        self.viz_tool = VisualizationTool()

        # Load OpenAI API key from environment variables
        openai.api_key = os.getenv('OPENAI_API_KEY')
        if not openai.api_key:
            logging.warning("OpenAI API key not set. Please check your .env file.")

        logging.info("Capstone Agent initialized.")

    def run_analysis(self):
        """
        Run data analysis and generate insights.

        Returns:
            dict: Summary statistics of the dataset.
        """
        if self.data_tool.data.empty:
            logging.error("No data available for analysis.")
            return {}

        summary = self.data_tool.get_summary_statistics()
        logging.info("Completed data summary.")
        return summary

    def visualize_data(self, x_column, y_column, chart_type='bar'):
        """
        Create a visualization based on the data.

        Args:
            x_column (str): Column for the x-axis.
            y_column (str): Column for the y-axis.
            chart_type (str): Type of chart to create (bar/line).

        Returns:
            str: Path to the saved visualization image.
        """
        if self.data_tool.data.empty:
            logging.error("No data available for visualization.")
            return None

        try:
            if chart_type == 'bar':
                return self.viz_tool.create_bar_chart(
                    self.data_tool.data, x_column, y_column, title='Bar Chart Visualization'
                )
            elif chart_type == 'line':
                return self.viz_tool.create_line_plot(
                    self.data_tool.data, x_column, y_column, title='Line Plot Visualization'
                )
            else:
                logging.error("Invalid chart type selected.")
                return None
        except Exception as e:
            logging.error(f"Error creating visualization: {e}")
            return None

    def summarize_data_with_openai(self):
        """
        Generate a summary of the dataset using OpenAI's GPT model.

        Returns:
            str: AI-generated summary of the dataset.
        """
        try:
            # Load API key from environment variable
            api_key = os.getenv('OPENAI_API_KEY')
            
            # Validate API key
            if not api_key or len(api_key.strip()) < 20:
                raise ValueError("Invalid or missing OpenAI API key. Please check your .env file.")

            # Create an OpenAI client
            client = openai.OpenAI(api_key=api_key)

            # Prepare the dataset summary for the prompt
            data_summary = self.data_tool.get_summary_statistics()
            
            # Construct a prompt for summarization
            prompt = f"""
            Analyze the following dataset statistics about heart attack risks in young individuals:
            {data_summary}

            Provide a concise summary that highlights:
            1. Key health trends
            2. Potential risk factors
            3. Insights for preventive healthcare
            """

            # Call OpenAI API using the new client method
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Updated to a chat model
                messages=[
                    {"role": "system", "content": "You are a professional healthcare data analyst."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                n=1,
                temperature=0.7
            )

            # Extract and return the summary
            summary = response.choices[0].message.content.strip()
            logging.info("AI-generated summary obtained successfully.")
            return summary
        
        except ValueError as ve:
            logging.error(f"Configuration error: {ve}")
            return f"Configuration error: {ve}"
        except Exception as e:
            # Catch-all for any other OpenAI-related errors
            logging.error(f"OpenAI API error: {e}", exc_info=True)
            return f"Error generating summary: {e}"

    def get_health_stats_from_api(self):
        """
        Call an external API to fetch health-related statistics.

        Returns:
           dict or str: Health statistics or an error message.
        """
        # Replace with a valid API URL
        api_url = "https://jsonplaceholder.typicode.com/posts"  # Example public API
    
        try:
            # Add a timeout to prevent hanging
            response = requests.get(api_url, timeout=10)
        
            # Check for successful response
            if response.status_code == 200:
                try:
                    # Attempt to parse the response as JSON
                    data = response.json()
                    summary = {
                        "total_records": len(data),
                        "sample_record": data[0] if len(data) > 0 else "No data found",
                        "data_source": "Example Public API"
                   }
                
                    logging.info("Successfully fetched and parsed API statistics.")
                    return summary
            
                except ValueError as json_err:
                    # If response is not valid JSON
                    logging.error(f"JSON parsing error: {json_err}")
                    return f"Error: Unable to parse API response - {json_err}"
        
            else:
                error_message = f"Error: Unable to fetch data, status code {response.status_code}"
                logging.error(error_message)
                return error_message
    
        except requests.exceptions.RequestException as req_err:
            # Handle network-related errors
            logging.error(f"Network error in API call: {req_err}")
            return f"Network error: {req_err}"
    
        except Exception as e:
            # Catch-all for any other unexpected errors
            logging.error(f"Unexpected error in API call: {e}")
            return f"Unexpected error: {e}"

