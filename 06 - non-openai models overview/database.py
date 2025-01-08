import pandas as pd
import sqlite3
import os

class SpaceMissionsDatabase:
    def __init__(self, csv_path):
        self.csv_path = csv_path  # Correct assignment
        self.conn = sqlite3.connect('space_missions.db')
        self.create_database()
    
    def create_database(self):
        # Read CSV and create SQLite database
        df = pd.read_csv(self.csv_path)
        df.to_sql('missions', self.conn, if_exists='replace', index=False)
    
    def query_missions(self, sql_query):
        return pd.read_sql_query(sql_query, self.conn)
    
    def close_connection(self):
        self.conn.close()