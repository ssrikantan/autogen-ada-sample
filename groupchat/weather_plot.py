# filename: weather_plot.py

import pandas as pd
import requests
from matplotlib import pyplot as plt

try:
    # Step 1: Download the data
    url = "https://raw.githubusercontent.com/vega/vega/main/docs/data/seattle-weather.csv"
    
    # Using pandas read_csv function to directly load data from the url
    df = pd.read_csv(url)
    
    # Step 2: Print the fields in the DataFrame
    print(df.columns.to_list())

    # Step 3: Count the amount of each weather and plot
    weather_count = df['weather'].value_counts()
    weather_count.plot(kind='bar')
    
    # Rotate x labels
    plt.xticks(rotation='vertical')

    # Step 4: Save the plot to a file
    plt.title('Amount of Each Weather Type in Seattle')
    plt.xlabel('Weather Type')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('weather_plot.png')
    print("Weather plot saved to: weather_plot.png")
    
except Exception as e:
    print(f"An error occurred: {e}")