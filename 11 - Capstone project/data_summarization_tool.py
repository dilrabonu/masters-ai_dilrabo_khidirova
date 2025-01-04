import pandas as pd
import os
from dotenv import load_dotenv
import logging

class DataSummarizationTool:
    def __init__(self):
        load_dotenv()
        file_path = os.getenv('DATA_FILE', 'heart_attack_youngsters_india.csv')
        self.data = pd.read_csv(file_path)

    def get_summary_statistics(self):
        if self.data.empty:
            return {}
        return {
            "Total Rows": len(self.data),
            "Columns": list(self.data.columns),
            "Description": self.data.describe().to_dict()
        }
