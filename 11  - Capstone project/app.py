import streamlit as st
from agent import process_query

def main():
    st.title("Logistics Agent")
    st.sidebar.header("Business Dashboard")
    st.sidebar.write("Additional business insights can be added here.")

    user_input = st.text_input("Enter a query: ")
    if st.button("Submit"):
        if user_input:
            response = process_query(user_input)
            st.write(f"Response: {response}")
        else:
            st.warning("Please enter a query")

if __name__ == "__main__":
    main()