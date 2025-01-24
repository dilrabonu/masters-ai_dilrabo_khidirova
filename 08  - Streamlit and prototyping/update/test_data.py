import os
import pandas as pd

# Resolve the absolute path of the dataset file
file_path = os.path.abspath('heart_attack_youngsters_india.csv')
print(f"Resolved file path: {file_path}")

# Check if the file exists
if os.path.exists(file_path):
    print("File exists. Attempting to load...")
    try:
        # Load the dataset using pandas
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully with {len(data)} rows.")
        print("First few rows of the dataset:")
        print(data.head())
    except Exception as e:
        print(f"Error loading the dataset: {e}")
else:
    print("File does not exist.")
