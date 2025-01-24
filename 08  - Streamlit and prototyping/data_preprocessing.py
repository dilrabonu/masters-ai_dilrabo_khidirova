import os
from dotenv import load_dotenv
import pandas as pd

class DataPreprocessor:
    def __init__(self, file_path=None):
        """
        Initialize data preprocessor for heart attack dataset
        """
        # Load environment variables
        load_dotenv()

        # Use file path from .env or default to provided path
        file_path = file_path or os.getenv('DATA_FILE', 'heart_attack_youngsters_india.csv')
        
        # Ensure absolute path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, file_path)
        
        self.raw_data = pd.read_csv(full_path)
        self.processed_data = None
