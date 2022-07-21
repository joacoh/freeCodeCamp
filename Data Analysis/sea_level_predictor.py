import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
# Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    xaxis = 'Year'
    yaxis = 'CSIRO Adjusted Sea Level'
# Create scatter plot
    x = df[xaxis]
    y = df[yaxis]
    plt.figure(figsize=(10,8))
    plt.scatter(x, y, color='mediumseagreen',label='Data')
# Create first line of best fit
    slp, inter, _, _, _ = linregress(x,y)
    xx = pd.Series([i for i in range(1880,2051)])
    yy = slp*xx + inter
    plt.plot(xx,yy, linestyle='--', color='k', label='Fit to 2050 (All Data)')
# Create second line of best fit
    df_recent = df.copy()
    df_recent = df_recent[df_recent['Year']>=2000]
    x = df_recent[xaxis]
    y = df_recent[yaxis]
    slp, inter, _, _, _ = linregress(x,y)
    xx = pd.Series([i for i in range(2000,2051)])
    yy = slp*xx + inter
    plt.plot(xx,yy, linestyle='-.', color='grey', label='Fit to 2050 (Recent Data)')
# Add labels and title
    plt.xlabel(xaxis)
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
# Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()