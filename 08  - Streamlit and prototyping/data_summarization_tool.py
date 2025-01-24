import os
from dotenv import load_dotenv
import pandas as pd
import logging

class DataSummarizationTool:
    def __init__(self, data_path=None):
        """
        Initialize the data summarization tool with a data source
        """
        try:
            # Load environment variables
            load_dotenv()

            # Use file path from .env or default to provided path
            data_path = data_path or os.getenv('DATA_FILE', 'heart_attack_youngsters_india.csv')
            
            # Ensure absolute path
            current_dir = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(current_dir, data_path)

            # Check if file exists
            if not os.path.exists(full_path):
                logging.error(f"Data file not found: {full_path}")
                self.data = pd.DataFrame()  # Create an empty DataFrame
                return

            self.data = pd.read_csv(full_path)
            logging.info(f"Successfully loaded data from {full_path}")
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            self.data = pd.DataFrame()  # Create an empty DataFrame
