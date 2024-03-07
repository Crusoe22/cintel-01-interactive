import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

with ui.sidebar():
    ui.input_slider(id="selected_number_of_bins", label="Number of Bins", min=0, max=100, value=20)


@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, bins=input.selected_number_of_bins(), density=True)
    plt.title('Histogram of Random Data')  # Added title to the histogram
    plt.xlabel('Value')
    plt.ylabel('Density')

# Function to generate a scatter plot
@render.plot(alt="Scatter plot")
def scatter_plot():
    np.random.seed(12345)
    x = np.random.normal(0, 1, 1000)
    y = np.random.normal(0, 1, 1000)
    plt.scatter(x, y, alpha=0.5)
    plt.title('Scatter Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
