**Capstone Project Data Analysis Agent**

Project Overview This capstone project aims to analyze a dataset of young individuals to assess their risk of heart attacks. The project includes data preprocessing, summarization, and visualization functionalities. It is designed to provide insights into the factors contributing to heart attack risks.
The project leverages Streamlit for an interactive user interface and tools for data preprocessing, summarization, and visualization.


**Features**

Functional Requirements Data Summarization: Provides high-level insights into the dataset, including total rows, columns, and descriptive statistics.
Visualization: Generates bar charts and line plots to visualize relationships in the dataset.
Data Preprocessing: Cleans data, handles missing values, and prepares datasets for machine learning. 
Action via API Calls: Demonstrates API integration to handle external functions. 
Business Information in UI: Displays preprocessing results and insights for decision-making.
Non-Functional Requirements Streamlit Interface: A modern and user-friendly web application. 
Logging: Provides detailed logs in the console for debugging and tracking application events. 
Python Version Compatibility: 
Supports Python versions <= 3.12. 
Function Calls: Incorporates multiple tools for API interactions and internal functionalities.


**Project Structure**

capstone_project/

│ ├── .env # Environment variables (e.g., data file path)

├── app.py # Main Streamlit application

├── agent.py # Agent logic for analysis and visualization

├── data_preprocessing.py # Handles data cleaning and preprocessing

├── data_summarization_tool.py # Provides summary statistics

├── visualization_tool.py # Generates visualizations (e.g., bar charts)

├── heart_attack_youngsters_india.csv # Dataset for analysis

├── requirements.txt # List of required Python packages

├── README.md # Documentation for the project

**Requirements**

streamlit==1.29.0
pandas==2.2.0
matplotlib==3.8.2
python-dotenv==1.0.0
openai==1.12.0
requests==2.31.0
numpy
scikit-learn



**Functional Details**

1.	Data Preprocessing Cleans missing values using imputation techniques. Encodes categorical variables for machine learning. Normalizes numerical features. Splits the dataset into training and testing sets.
2.	Data Summarization Provides an overview of the dataset: Total number of rows and columns. Summary statistics (e.g., mean, median, standard deviation).
3.	Visualization Generates bar and line charts. Saves visualizations as images in the visualizations/ folder.
Tools and Libraries Python Libraries: Streamlit: For creating the web application. Pandas: For data manipulation and analysis. Matplotlib: For creating visualizations. Scikit-Learn: For data preprocessing and splitting. Python-Dotenv: For managing environment variables.
Example Dataset The dataset, heart_attack_youngsters_india.csv, contains information on:
Demographics: Age, gender, etc. Health Factors: BMI, smoking habits, physical activity. Target Variable: Likelihood of heart attack.

**Installation**

1.	Clone the repository
2.	Create a virtual environment:
   
**Used CSV file from this website**

https://www.kaggle.com/datasets/ankushpanday1/heart-attack-in-youth-of-india
