import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x, y = df['Year'], df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    reg = linregress(x, y)
    predicted_years = np.arange(1880, 2050, 1)
    plt.plot(predicted_years, reg.intercept + reg.slope*predicted_years, 'r')


    # Create second line of best fit
    predicted_years2 = np.arange(2000, 2050, 1)
    filtered = df[df['Year'] >= 2000]
    x2 = filtered['Year']
    y2 = filtered['CSIRO Adjusted Sea Level']
    reg2 = linregress(x2, y2)
    plt.plot(predicted_years2, reg2.intercept + reg2.slope*predicted_years2, 'r')


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")    
    #plt.show()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()