import sqlite3
import pandas as pd
from datetime import datetime

DB_NAME = 'weather_data.db'
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

def get_daily_summary():
    """Generate daily summary with aggregate calculations."""
    # Use DATE('now', 'localtime') to get today's date in local timezone
    c.execute(f"""
        SELECT city, temperature, weather_condition 
        FROM weather 
        WHERE DATE(datetime(timestamp, 'unixepoch'), 'localtime') = DATE('now', 'localtime')
    """)
    data = c.fetchall()
    
    print("Data fetched from database:", data)  # Debugging line
    
    if not data:
        print("No data for today.")
        return
    
    # Create DataFrame with the correct column names
    df = pd.DataFrame(data, columns=['city', 'temperature', 'weather_condition'])
    
    # Calculate aggregates
    avg_temp = df['temperature'].mean()
    max_temp = df['temperature'].max()
    min_temp = df['temperature'].min()
    dominant_weather = df['weather_condition'].mode()[0]  # Most frequent weather condition
    
    today = datetime.now().strftime('%Y-%m-%d')
    print(f"Daily Summary for {today}")
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print(f"Max Temperature: {max_temp:.2f}°C")
    print(f"Min Temperature: {min_temp:.2f}°C")
    print(f"Dominant Weather Condition: {dominant_weather}")
    
    return {
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_weather': dominant_weather
    }

if __name__ == '__main__':
    summary = get_daily_summary()
