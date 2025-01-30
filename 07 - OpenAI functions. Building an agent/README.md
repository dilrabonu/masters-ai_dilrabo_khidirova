# AI Health Data Assistant

## Overview
This AI agent assists users in querying heart attack risk factors from a structured health dataset. It utilizes OpenAI's GPT API and SQLite for efficient querying, and includes an additional function for sending alerts to a third-party API.

## Project Structure
```
/your_project_directory
│── db/
│   ├── heart_attack_data.sqlite
│── .env
│── conversation.py
│── main.py
│── requirements.txt
│── README.md
```

## Installation
1. **Clone the repository**
   ```bash
   git clone <repo_url>
   cd your_project_directory
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the root directory and add:
     ```bash
     OPENAI_API_KEY=your_openai_api_key
     ```

## Running the Application
1. **Run the Streamlit app**
   ```bash
   streamlit run main.py
   ```
2. **Interact with the AI agent**
   - Enter queries about heart attack risk factors.
   - The AI will generate SQL queries and fetch relevant data.
   - Alerts can be triggered based on detected health risks.

## Features
- **AI-driven database queries**: Users can ask health-related questions, and the AI will retrieve relevant data.
- **Function calling**: Calls a third-party API for sending health alerts.
- **Interactive UI**: Built with Streamlit for ease of use.

## Future Enhancements
- Improve natural language processing for better query handling.
- Expand database with additional health metrics.
- Integrate visualization tools for insights.

## License
This project is licensed under the MIT License.

