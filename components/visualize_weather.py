import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

DB_NAME = 'weather_data.db'
print("Plotting temperature trends for the last 24 hours...")

def plot_weather_trends():
    """Plot temperature trends for the last 24 hours."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Set the current time and 24 hours ago
    end_time = datetime.now()
    start_time = end_time - timedelta(days=1)
    
    # Convert start and end times to Unix timestamps
    start_timestamp = int(start_time.timestamp())
    end_timestamp = int(end_time.timestamp())
    
    # Fetch distinct data for the last 24 hours, avoiding duplicates
    c.execute("""
        SELECT DISTINCT city, temperature, timestamp 
        FROM weather 
        WHERE timestamp BETWEEN ? AND ?
        ORDER BY city, timestamp
    """, (start_timestamp, end_timestamp))
    
    data = c.fetchall()
    conn.close()

    if not data:
        print("No data for the last 24 hours.")
        return

    # Load data into a pandas DataFrame
    df = pd.DataFrame(data, columns=['city', 'temp', 'timestamp'])
    
    # Convert the timestamp back to a readable format
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    # Plot temperature trends
    plt.figure(figsize=(10, 6))
    
    # Iterate through each city to plot
    for city in df['city'].unique():
        city_data = df[df['city'] == city]
        plt.plot(city_data['timestamp'], city_data['temp'], label=city)
    
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Trends for the Last 24 Hours')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    plot_weather_trends()
