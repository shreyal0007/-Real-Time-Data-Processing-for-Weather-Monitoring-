import sqlite3
from datetime import datetime

DB_NAME = 'weather_data.db'
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()


DB_NAME = 'weather_data.db'
ALERT_THRESHOLD_TEMP = 35.0 

conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

def check_thresholds():
    """Check for temperature alerts."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    c.execute("SELECT city, temperature, timestamp FROM weather ORDER BY timestamp DESC LIMIT 12")  # Last 12 data points
    data = c.fetchall()
    conn.close()  

    alerts = []
    
    # Ensure we have enough data points to check for consecutive readings
    if len(data) < 2:
        print("Not enough data to check for temperature thresholds.")
        return

    # Iterate over data in pairs
    for i in range(0, len(data) - 1, 2):  
        city = data[i][0]
        temp_latest = data[i][1]
        temp_prev = data[i + 1][1]
        
        if temp_latest > ALERT_THRESHOLD_TEMP and temp_prev > ALERT_THRESHOLD_TEMP:
            alerts.append(f"Alert! Temperature in {city} exceeded {ALERT_THRESHOLD_TEMP}°C for two consecutive readings.")
    
    # Check for any alerts and print them
    if alerts:
        for alert in alerts:
            print(alert)
    else:
        print("No threshold breaches detected.")

if __name__ == '__main__':
    check_thresholds()
