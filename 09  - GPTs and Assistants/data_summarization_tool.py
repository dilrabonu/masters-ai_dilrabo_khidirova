import os
import logging
import pandas as pd
from dotenv import load_dotenv

class DataSummarizationTool:
    def __init__(self, data_path=None):
        """
        Initialize the data summarization tool with a data source.
        """
        try:
            # Load environment variables from the .env file
            load_dotenv()

            # Resolve the dataset path
            if not data_path:
                # Use the environment variable or a default filename
                data_path = os.getenv('DATA_FILE', 'heart_attack_youngsters_india.csv')

            # Log the initial data path
            logging.info(f"Attempting to load data from path: {data_path}")

            # Ensure absolute path
            current_dir = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(current_dir, data_path)
            
            # Additional logging for path resolution
            logging.info(f"Current directory: {current_dir}")
            logging.info(f"Resolved full path: {full_path}")

            # Check if the file exists
            if not os.path.exists(full_path):
                # Try alternative path resolution
                full_path = os.path.abspath(data_path)
                logging.warning(f"First path not found. Trying alternative path: {full_path}")

                if not os.path.exists(full_path):
                    logging.error(f"Data file not found at {full_path}")
                    self.data = pd.DataFrame()  # Return an empty DataFrame
                    return

            # Log success in locating the file
            logging.info(f"File exists at path: {full_path}")

            # Load the dataset
            self.data = pd.read_csv(full_path)

            # Check if the dataset is empty
            if self.data.empty:
                logging.error(f"Loaded data is empty: {full_path}")
            else:
                logging.info(f"Successfully loaded data from {full_path} with {len(self.data)} rows.")
        except Exception as e:
            logging.error(f"Comprehensive error loading data: {e}", exc_info=True)
            self.data = pd.DataFrame()  # Return an empty DataFrame in case of errors

    def get_summary_statistics(self):
        """
        Get summary statistics for the loaded dataset.

        Returns:
            dict: Summary statistics of the dataset.
        """
        if self.data.empty:
            logging.warning("No data available for summary statistics.")
            return {}

        try:
            # Compute summary statistics
            summary = self.data.describe(include='all').to_dict()
            logging.info("Summary statistics generated successfully.")
            return summary
        except Exception as e:
            logging.error(f"Error generating summary statistics: {e}")
            return {}
