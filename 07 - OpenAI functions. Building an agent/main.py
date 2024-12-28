import os
import sqlite3
import openai
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'database.sqlite')
TABLE_NAME = 'animals_info'

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError("No OpenAI API key found. Please set OPENAI_API_KEY in .env file.")

# Function to execute SQL queries
def execute_query(query):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        return [dict(zip(column_names, row)) for row in rows]
    except sqlite3.Error as e:
        return {"error": str(e)}
    finally:
        if conn:
            conn.close()

# Flask endpoint to handle user questions
@app.route('/query', methods=['POST'])
def query_database():
    user_input = request.json.get('question')
    if not user_input:
        return jsonify({"error": "No question provided"}), 400

    try:
        # Use OpenAI to generate SQL query
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant that generates SQL queries based on user questions."},
                {"role": "user", "content": f"Generate an SQL query for the following question: {user_input}. Assume the table name is {TABLE_NAME}."}
            ]
        )

        sql_query = response['choices'][0]['message']['content'].strip()
        print(f"Generated SQL Query: {sql_query}")

        # Execute the generated SQL query
        results = execute_query(sql_query)

        return jsonify({
            'question': user_input,
            'results': results
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add routes for root URL and favicon
@app.route('/')
def index():
    return "Welcome to the Animal Database Query API! Use /query endpoint to ask questions."

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return an empty response with 204 No Content status

# Run the app
if __name__ == '__main__':
    app.run(port=5000, debug=True)