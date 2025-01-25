import os
import sqlite3
import pandas as pd

def setup_database():
    # Construct the full path to the current directory and files
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(base_dir, "heart_attack_youngsters_india.csv")
    db_file = os.path.join(base_dir, "heart_attack.db")

    print(f"Base Directory: {base_dir}")
    print(f"CSV File Path: {csv_file}")
    print(f"Database File Path: {db_file}")

    # Check if the CSV file exists
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"CSV file not found: {csv_file}. Current directory contents: {os.listdir(base_dir)}")

    # Establish SQLite connection
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Define the table schema
    print("Creating table schema...")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS heart_attack_data (
        id INTEGER PRIMARY KEY,
        age INTEGER,
        gender TEXT,
        region TEXT,
        cholesterol_level REAL,
        blood_pressure REAL,
        heart_attack_likelihood TEXT
    )
    """)

    # Load data from CSV
    try:
        print("Loading data from CSV...")
        df = pd.read_csv(csv_file)

        # Rename columns to match the expected schema
        df.rename(columns={
            "Age": "age",
            "Gender": "gender",
            "Region": "region",
            "Cholesterol Levels (mg/dL)": "cholesterol_level",
            "Heart Attack Likelihood": "heart_attack_likelihood"
        }, inplace=True)

        # Extract average blood pressure from 'Blood Pressure (systolic/diastolic mmHg)'
        def extract_avg_bp(bp_str):
            try:
                systolic, diastolic = map(int, bp_str.split('/'))
                return (systolic + diastolic) / 2
            except:
                return None

        df["blood_pressure"] = df["Blood Pressure (systolic/diastolic mmHg)"].apply(extract_avg_bp)

        # Select only the required columns
        df = df[["age", "gender", "region", "cholesterol_level", "blood_pressure", "heart_attack_likelihood"]]

        # Add an 'id' column if it doesn't exist
        if 'id' not in df.columns:
            print("Adding 'id' column to the data...")
            df.reset_index(inplace=True)
            df.rename(columns={'index': 'id'}, inplace=True)

        # Save data to SQLite
        print(f"Saving {len(df)} rows to the database...")
        df.to_sql("heart_attack_data", conn, if_exists="replace", index=False)
        print(f"Database setup complete. Database saved at: {db_file}")

    except Exception as e:
        print(f"Error loading data from CSV: {e}")

    finally:
        conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    setup_database()
