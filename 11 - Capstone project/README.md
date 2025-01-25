**Heart Attack Risk Analysis**

**Project Overview**
The Heart Attack Risk Analysis project is a web-based application built to analyze risk factors associated with heart attacks among young individuals in India. The application enables users to query a database of health and lifestyle metrics to gain insights into heart attack likelihood based on various factors such as cholesterol levels, blood pressure, stress, and more.

**Features
Query the Database:**

Users can input SQL queries to analyze the dataset dynamically.
Supports advanced queries, grouping, and aggregation for detailed insights.
Interactive Web Application:
Built using Streamlit for a user-friendly interface.
Displays query results in a clean and tabular format.
Comprehensive Dataset:
Includes key metrics such as cholesterol levels, blood pressure, lifestyle factors, and more.
Derived from real-world data of young individuals in India.


**Technologies Used**

Python:
Backend scripting and database interactions.

SQLite:
Lightweight relational database for storing and querying data.

Pandas:
Data manipulation and preprocessing.

Streamlit:
Web-based interface for querying and visualizing the data.

OpenAI GPT-4:
Integrated for natural language processing (if applicable).

Environment Management:
dotenv for managing API keys securely.

Setup Instructions
Follow these steps to set up and run the application locally:

**Clone the Repository:**

Install Dependencies: Create and activate a virtual environment:
Install the required Python packages:

**Set Up the Database:**

Ensure the dataset file (heart_attack_youngsters_india.csv) is in the database directory.
Run the db_setup.py script to set up the SQLite database:

**Run the Application: Launch the Streamlit app:**

**Project Files**

app.py:
Main application file for Streamlit.

db_setup.py:
Script to set up the SQLite database from the dataset.

heart_attack.db:
SQLite database storing the processed data.

requirements.txt:
List of Python dependencies.

Dataset:
heart_attack_youngsters_india.csv: Source data used for analysis.

**Data Website:**
https://www.kaggle.com/datasets/ankushpanday1/heart-attack-in-youth-of-india


