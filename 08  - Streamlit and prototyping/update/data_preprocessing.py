import os
from dotenv import load_dotenv
import pandas as pd
from sklearn.model_selection import train_test_split

class DataPreprocessor:
    def __init__(self, file_path=None):
        """
        Initialize the data preprocessor for the heart attack dataset.
        """
        load_dotenv()

        # Use file path from .env or default to provided path
        file_path = file_path or os.getenv('DATA_FILE', 'heart_attack_youngsters_india.csv')

        # Ensure absolute path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, file_path)

        try:
            # Load the dataset
            self.raw_data = pd.read_csv(full_path)

            # Clean column names by stripping any extra spaces
            self.raw_data.columns = self.raw_data.columns.str.strip()

            # Check if the dataset is empty
            if self.raw_data.empty:
                raise ValueError(f"The dataset at {full_path} is empty.")
            
            print(f"Dataset loaded successfully from {full_path} with {len(self.raw_data)} rows.")
        except Exception as e:
            print(f"Error loading dataset: {e}")
            self.raw_data = pd.DataFrame()

    def prepare_ml_dataset(self, target_column='Heart Attack Likelihood'):
        """
        Prepares the dataset for machine learning by splitting into training and test sets.
        Args:
            target_column (str): The name of the target column to predict.
        Returns:
            X_train, X_test, y_train, y_test: Training and testing datasets.
        """
        # Ensure the target column exists
        if target_column not in self.raw_data.columns:
            raise ValueError(f"Target column '{target_column}' not found in the dataset.")

        try:
            # Convert target column values to numeric (e.g., Yes -> 1, No -> 0)
            self.raw_data[target_column] = self.raw_data[target_column].map({'Yes': 1, 'No': 0})

            # Ensure no missing values in the target column after conversion
            if self.raw_data[target_column].isnull().any():
                raise ValueError(f"The target column '{target_column}' contains invalid or missing values.")

            # Split into features (X) and target (y)
            X = self.raw_data.drop(columns=[target_column])
            y = self.raw_data[target_column]

            # Split into training and test sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            print(f"Data split successfully: {X_train.shape[0]} training rows, {X_test.shape[0]} testing rows.")
            return X_train, X_test, y_train, y_test

        except Exception as e:
            raise ValueError(f"Error during dataset preparation: {e}")
