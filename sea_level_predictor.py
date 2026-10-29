import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # --- CREATE SCATTERPLOT ---
    fig, ax = plt.subplots(1,1)
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # --- CREATE FIRST LINE OF BEST FIT ---
    lin_2050 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create new years (x-axis)
    extended_years = np.arange(1880, 2051)

    # Create new values (y-axis) using y=mx+b
    values_all = lin_2050.slope * extended_years + lin_2050.intercept

    # plot the line of best fit
    ax.plot(extended_years, values_all, color="red", label="Fit Line (All Data)")

    # extend x-axis limit to show 2050 (and extra space beyond)
    ax.set_xlim(1850, 2075)


    # --- CREATE SECOND LINE OF BEST FIT ---
    # filter by 2000 and on
    df_recent = df[df['Year']>=2000].copy()

    # Create second line of best fit using filtered df
    lin_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Create new years starting from 2000 (x-axis)
    extended_years_recent = np.arange(2000, 2051)

    # Create new values (y-axis) using years starting from 2000 and on
    values_recent = lin_recent.slope * extended_years_recent + lin_recent.intercept

    # plot the line of best fit
    ax.plot(extended_years_recent, values_recent, color="green", label="Fit Line (Start Year=2000)")

    
    # --- ADD LABELS AND TITLE ---
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    plt.show()
    return plt.gca()