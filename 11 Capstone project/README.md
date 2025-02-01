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

├── pictures                  # Screenshot

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
![image](https://github.com/user-attachments/assets/372d230f-aadc-4cab-901e-ce1ae859fdc9)
![image](https://github.com/user-attachments/assets/b0b04ebc-3ca0-44a8-9c9c-ebf2d887a335)
![image](https://github.com/user-attachments/assets/249ef264-c10a-488f-a306-525fa9e3b3a9)
![image](https://github.com/user-attachments/assets/b6d89d60-d232-4398-a5aa-910899f8dddd)
![image](https://github.com/user-attachments/assets/4e490b7f-4999-444d-afbf-bfe1325d3dee)
![image](https://github.com/user-attachments/assets/0c3e9bef-778c-44e0-ba05-ad2432dd29b4)
![image](https://github.com/user-attachments/assets/9017ea3a-3927-4606-9f97-1a35a4800782)
![image](https://github.com/user-attachments/assets/bf703f43-02a8-44e6-9b77-91837e2d1f61)









**Website:**
https://www.kaggle.com/datasets/ankushpanday1/heart-attack-in-youth-of-india
