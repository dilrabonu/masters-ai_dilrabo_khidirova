import streamlit as st
from agent import main as run_app
from data_preprocessing import DataPreprocessor
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s: %(message)s')

def preprocess_and_display_data():
    """
    Preprocess the dataset and display preprocessing results
    """
    try:
        # Initialize preprocessor
        preprocessor = DataPreprocessor('heart_attack_youngesters_india.csv')
        
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
    Main application entry point
    """
    st.sidebar.title("Heart Attack Risk Analysis")
    
    # Sidebar menu
    menu = st.sidebar.radio(
        "Navigation", 
        ["Data Analysis App", "Preprocessing Results"]
    )
    
    if menu == "Data Analysis App":
        run_app()
    elif menu == "Preprocessing Results":
        preprocess_and_display_data()

if __name__ == "__main__":
    main()