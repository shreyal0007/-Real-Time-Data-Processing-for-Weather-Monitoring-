import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

DB_NAME = 'weather_data.db'

def plot_weather_trends():
    """Plot temperature trends for the last 24 hours."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    end_time = datetime.now()
    start_time = end_time - timedelta(days=1)
    
    # Fetch data for the last 24 hours
    c.execute("SELECT city, temperature, timestamp FROM weather WHERE timestamp BETWEEN ? AND ?", 
              (start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S')))
    data = c.fetchall()
    conn.close()  # Close the connection after fetching data

    if not data:
        print("No data for the last 24 hours.")
        return

    df = pd.DataFrame(data, columns=['city', 'temp', 'timestamp'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Plot temperature trends
    plt.figure(figsize=(10, 6))
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
    plot_weather_trends()  # Plot the weather trends
