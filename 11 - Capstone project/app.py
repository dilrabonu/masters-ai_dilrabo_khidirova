import streamlit as st
import sqlite3
import pandas as pd
from agent.agent import chat_with_function_calling

# Set the page title
st.title("Heart Attack Risk Analysis")

# Function to query the database
def query_database(query):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('heart_attack.db')
        cursor = conn.cursor()

        # Execute the query and fetch results
        cursor.execute(query)
        results = cursor.fetchall()

        # Fetch column names for tabular display
        column_names = [description[0] for description in cursor.description]

        # Close the connection
        conn.close()

        # Return results as a DataFrame
        return pd.DataFrame(results, columns=column_names)
    except sqlite3.Error as e:
        raise Exception(f"Database error: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")

# Sidebar for user input
st.sidebar.header("Query the Database")
user_query = st.sidebar.text_area("Ask something about the data (SQL query):")

# Submit button
if st.sidebar.button("Submit"):
    if user_query.strip():
        try:
            # Allow users to query the database directly
            st.subheader("SQL Query Results:")
            query_results = query_database(user_query)

            if not query_results.empty:
                st.write(query_results)
            else:
                st.warning("The query returned no results.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid SQL query.")

# Provide a sample query for users
st.sidebar.markdown("""
### Sample Queries:
- `SELECT * FROM heart_attack_data LIMIT 5;`
- `SELECT COUNT(*) FROM heart_attack_data;`
- `SELECT region, AVG(cholesterol_level) AS avg_cholesterol FROM heart_attack_data GROUP BY region;`
""")
