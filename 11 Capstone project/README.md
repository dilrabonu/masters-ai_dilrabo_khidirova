**Agent AI Capstone Project**

**Project Overview**

This project is an AI-powered agent that assists users in retrieving and analyzing data from a structured SQLite database. The agent processes user queries, retrieves relevant data, and presents insights through a Streamlit-based user interface.

**Functional Requirements**

The agent extracts relevant data from the SQLite database and only passes necessary information to the LLM.

The agent is capable of calling external APIs to perform actions beyond its own capabilities.

The user interface provides insights beyond just chatbot responses, displaying relevant business information.

The agent logs all interactions and function executions to the console for debugging and monitoring.

**Non-Functional Requirements**

The agent is built using Python (<= 3.12).

The user interface is implemented using Streamlit.

The project integrates at least two different function-calling mechanisms.

The installation and setup instructions are provided in this README.

**Features**

Database Querying: Retrieves health data based on user queries using SQL.

Dataset Analysis: Computes statistical insights on heart attack risks.

Logging: All queries and system activities are logged for monitoring.

Conversational Interface: Provides structured responses based on queries.

Function Execution: Calls external APIs for advanced functionalities.*
**Installation**

**File Structure:**
.

├── main.py                # Streamlit UI implementation
├── conversation.py        # Conversation management
├── requirements.txt       # Required dependencies
├── heart_attack_data.sqlite # SQLite Database file
├── heart_attack_youngsters_india.csv # Dataset
├── .env                   # Environment variables (API keys)
└── README.md              # Documentation

**Usage**

Open the Streamlit UI.

Enter questions related to heart attack risks and health insights.

The agent will query the database and return structured responses.

The conversation history and function outputs will be displayed.

**API Function Calls**

The agent can execute the following function calls:

ask_database: Queries health data based on structured SQL queries.

analyze_dataset: Computes insights such as high-risk percentages and distributions.

**Website:**
https://www.kaggle.com/datasets/ankushpanday1/heart-attack-in-youth-of-india
