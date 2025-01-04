import matplotlib.pyplot as plt
import os

class VisualizationTool:
    def __init__(self):
        self.output_dir = "visualizations"
        os.makedirs(self.output_dir, exist_ok=True)

    def create_bar_chart(self, data, x_column, y_column):
        path = os.path.join(self.output_dir, "bar_chart.png")
        data.plot(kind='bar', x=x_column, y=y_column)
        plt.savefig(path)
        plt.close()
        return path
