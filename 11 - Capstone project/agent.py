import logging
import streamlit as st
from data_summarization_tool import DataSummarizationTool
from visualization_tool import VisualizationTool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class CapstoneAgent:
    def __init__(self):
        self.data_tool = DataSummarizationTool()
        self.viz_tool = VisualizationTool()

    def run_analysis(self):
        summary = self.data_tool.get_summary_statistics()
        return summary

    def visualize_data(self, x_column, y_column, chart_type='bar'):
        if self.data_tool.data.empty:
            st.error("No data available for visualization.")
            return None

        if chart_type == 'bar':
            return self.viz_tool.create_bar_chart(self.data_tool.data, x_column, y_column)
        elif chart_type == 'line':
            return self.viz_tool.create_line_plot(self.data_tool.data, x_column, y_column)

def main():
    st.title("Heart Attack Analysis for Young Individuals")
    agent = CapstoneAgent()

    if st.sidebar.button("Get Data Summary"):
        summary = agent.run_analysis()
        st.write("Data Summary:", summary)

    if not agent.data_tool.data.empty:
        columns = list(agent.data_tool.data.columns)
        x_col = st.sidebar.selectbox("X-axis Column", columns)
        y_col = st.sidebar.selectbox("Y-axis Column", columns)
        chart_type = st.sidebar.selectbox("Chart Type", ["bar", "line"])

        if st.sidebar.button("Create Visualization"):
            path = agent.visualize_data(x_col, y_col, chart_type)
            if path:
                st.image(path)
