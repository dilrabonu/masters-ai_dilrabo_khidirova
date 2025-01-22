import streamlit as st
import logging
from data_summarization_tool import DataSummarizationTool
from visualization_tool import VisualizationTool
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

# Configure logging securely
LOG_FILE = os.getenv("LOG_FILE", "app.log")
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

class CapstoneAgent:
    def __init__(self, data_path=os.getenv("DATA_PATH", "heart_attack_youngesters_india.csv")):
        """
        Initialize the Capstone Agent with tools
        
        Args:
            data_path (str): Path to the data file
        """
        # Validate data path
        if not os.path.exists(data_path):
            logging.error(f"Data file not found at {data_path}")
            raise FileNotFoundError("Data file is missing")

        # Initialize data summarization tool
        self.data_tool = DataSummarizationTool(data_path)
        
        # Initialize visualization tool
        self.viz_tool = VisualizationTool()
        
        logging.info("Capstone Agent initialized")
    
    def validate_data_integrity(self):
        """
        Validate dataset integrity to prevent poisoning.
        """
        if self.data_tool.data.empty:
            raise ValueError("Dataset is empty or corrupted")
        
        # Example: Check for missing values
        if self.data_tool.data.isnull().sum().sum() > 0:
            logging.warning("Dataset contains missing values")
            st.warning("Dataset has missing values. Consider cleaning it.")
        else:
            logging.info("Data integrity validated")

    def run_analysis(self):
        """
        Run data analysis and generate insights
        
        Returns:
            dict: Summary statistics of the dataset
        """
        self.validate_data_integrity()
        summary = self.data_tool.get_summary_statistics()
        logging.info("Completed data summary")
        return summary
    
    def visualize_data(self, x_column, y_column, chart_type='bar'):
        """
        Create visualization based on data
        
        Args:
            x_column (str): Column for x-axis
            y_column (str): Column for y-axis
            chart_type (str): Type of chart to create
        
        Returns:
            str: Path to visualization
        """
        self.validate_data_integrity()

        if chart_type == 'bar':
            return self.viz_tool.create_bar_chart(
                self.data_tool.data, 
                x_column, 
                y_column, 
                title='Data Visualization'
            )
        elif chart_type == 'line':
            return self.viz_tool.create_line_plot(
                self.data_tool.data, 
                x_column, 
                y_column, 
                title='Data Visualization'
            )

def main():
    st.title("Heart Attack Analysis for Young Individuals")
    
    # Initialize agent
    agent = CapstoneAgent()
    
    # Sidebar for interactions
    st.sidebar.header("Data Analysis Options")
    
    # Validate dataset
    try:
        agent.validate_data_integrity()
    except ValueError as e:
        st.error(str(e))
        return
    
    # Summary Statistics
    if st.sidebar.button("Get Data Summary"):
        summary = agent.run_analysis()
        st.write("Data Summary:", summary)
    
    # Visualization
    columns = list(agent.data_tool.data.columns)
    x_col = st.sidebar.selectbox("X-axis Column", columns)
    y_col = st.sidebar.selectbox("Y-axis Column", columns)
    chart_type = st.sidebar.selectbox("Chart Type", ["bar", "line"])
    
    if st.sidebar.button("Create Visualization"):
        viz_path = agent.visualize_data(x_col, y_col, chart_type)
        if viz_path:
            st.image(viz_path)

if __name__ == "__main__":
    main()
