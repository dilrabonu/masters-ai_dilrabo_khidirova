import streamlit as st
from agent import CapstoneAgent
from data_preprocessing import DataPreprocessor
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s: %(message)s')

def preprocess_and_display_data():
    """
    Preprocess the dataset and display preprocessing results.
    """
    try:
        # Initialize preprocessor
        preprocessor = DataPreprocessor('heart_attack_youngsters_india.csv')

        # Prepare ML dataset
        X_train, X_test, y_train, y_test = preprocessor.prepare_ml_dataset()

        # Display preprocessing results
        st.header("Data Preprocessing Results")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Training Set")
            st.write("Shape:", X_train.shape)
            st.write("Target Distribution:")
            st.dataframe(y_train.value_counts(normalize=True))

        with col2:
            st.subheader("Test Set")
            st.write("Shape:", X_test.shape)
            st.write("Target Distribution:")
            st.dataframe(y_test.value_counts(normalize=True))

        logging.info("Data preprocessing completed successfully")

    except Exception as e:
        st.error(f"Error in data preprocessing: {e}")
        logging.error(f"Preprocessing failed: {e}")

def main():
    """
    Main application entry point.
    """
    st.title("Heart Attack Risk Analysis for Young Individuals")

    # Initialize agent
    agent = CapstoneAgent()

    # Test if dataset is loaded
    if agent.data_tool.data.empty:
        st.error("No data loaded. Please check your dataset file.")
        return

    # Sidebar navigation
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio(
        "Options",
        ["Data Analysis App", "Preprocessing Results", "AI Summary", "API Insights"]
    )

    # Navigation logic
    if menu == "Data Analysis App":
        # Display dataset summary
        if st.sidebar.button("Get Data Summary"):
            summary = agent.run_analysis()
            st.write("Dataset Summary:")
            st.json(summary)

        # Visualization options
        columns = list(agent.data_tool.data.columns)
        x_col = st.sidebar.selectbox("X-axis Column", columns)
        y_col = st.sidebar.selectbox("Y-axis Column", columns)
        chart_type = st.sidebar.selectbox("Chart Type", ["bar", "line"])

        if st.sidebar.button("Create Visualization"):
            viz_path = agent.visualize_data(x_col, y_col, chart_type)
            if viz_path:
                st.image(viz_path)

    elif menu == "Preprocessing Results":
        preprocess_and_display_data()

    elif menu == "AI Summary":
        st.subheader("AI Summary")
        summary = agent.summarize_data_with_openai()
        st.write("AI-Generated Summary:")
        st.write(summary)

    elif menu == "API Insights":
        st.subheader("Health API Insights")
        api_results = agent.get_health_stats_from_api()
        st.write("API Results:")
        st.json(api_results)

if __name__ == "__main__":
    main()
