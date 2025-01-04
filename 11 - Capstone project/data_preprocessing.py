import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from dotenv import load_dotenv

class DataPreprocessor:
    def __init__(self):
        load_dotenv()
        file_path = os.getenv('DATA_FILE', 'heart_attack_youngsters_india.csv')
        self.raw_data = pd.read_csv(file_path)

    def clean_data(self):
        imputer = SimpleImputer(strategy='most_frequent')
        self.raw_data.fillna(imputer.fit_transform(self.raw_data))
        return self.raw_data

    def prepare_ml_dataset(self):
        self.clean_data()
        X = self.raw_data.drop(columns=['Heart Attack Likelihood'])
        y = self.raw_data['Heart Attack Likelihood']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
