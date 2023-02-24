import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope = result.slope
    intercept = result.intercept
    df = pd.concat([df, pd.DataFrame({'Year':range(2014, 2051)})])
    df['Prediction'] = slope * df['Year'] + intercept
    ax.plot('Year','Prediction',data=df, color='red')

    # Create second line of best fit
    df2 = df[(df['Year'] > 1999) & (df['Year'] < 2014)]
    result2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    slope2 = result2.slope
    intercept2 = result2.intercept
    df2 = pd.concat([df2, pd.DataFrame({'Year':range(2014, 2051)})])
    df2['Prediction'] = slope2 * df2['Year'] + intercept2
    ax.plot('Year','Prediction',data=df2, color='green')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
