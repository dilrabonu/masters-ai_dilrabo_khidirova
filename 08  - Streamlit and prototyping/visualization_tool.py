import matplotlib.pyplot as plt
import logging
import os
import pandas as pd

class VisualizationTool:
    def __init__(self, output_dir='visualizations'):
        """
        Initialize visualization tool
        
        Args:
            output_dir (str): Directory to save visualizations
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        logging.info(f"Visualization output directory: {output_dir}")
    
    def create_bar_chart(self, data, x_column, y_column, title='Bar Chart'):
        """
        Create a bar chart from the given data
        
        Args:
            data (pd.DataFrame): Input dataframe
            x_column (str): Column for x-axis
            y_column (str): Column for y-axis
            title (str): Chart title
        
        Returns:
            str: Path to saved visualization
        """
        try:
            plt.figure(figsize=(10, 6))
            data.plot(kind='bar', x=x_column, y=y_column)
            plt.title(title)
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.tight_layout()
            
            output_path = os.path.join(self.output_dir, f'{title.lower().replace(" ", "_")}.png')
            plt.savefig(output_path)
            plt.close()
            
            logging.info(f"Created bar chart: {output_path}")
            return output_path
        except Exception as e:
            logging.error(f"Error creating bar chart: {e}")
            return None
    
    def create_line_plot(self, data, x_column, y_column, title='Line Plot'):
        """
        Create a line plot from the given data
        
        Args:
            data (pd.DataFrame): Input dataframe
            x_column (str): Column for x-axis
            y_column (str): Column for y-axis
            title (str): Plot title
        
        Returns:
            str: Path to saved visualization
        """
        try:
            plt.figure(figsize=(12, 6))
            plt.plot(data[x_column], data[y_column])
            plt.title(title)
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.tight_layout()
            
            output_path = os.path.join(self.output_dir, f'{title.lower().replace(" ", "_")}_line.png')
            plt.savefig(output_path)
            plt.close()
            
            logging.info(f"Created line plot: {output_path}")
            return output_path
        except Exception as e:
            logging.error(f"Error creating line plot: {e}")
            return None