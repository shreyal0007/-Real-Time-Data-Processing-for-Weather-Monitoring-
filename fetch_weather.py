import requests
import sqlite3
import time
import schedule

API_KEY = 'f67941801869246c922a22f028d26bed' 
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
DB_NAME = 'weather_data.db'

def create_table():
    """Create the weather table if it does not exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            temperature REAL,
            feels_like REAL,
            weather_condition TEXT,
            timestamp INTEGER
        )
    ''')
    conn.commit()
    conn.close()
    print("Weather table created or already exists.")

def fetch_weather_data():
    """Fetch weather data for each city and store it in the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    for city in CITIES:
        print(f"Fetching weather data for {city}...")
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                temp = data['main']['temp']
                feels_like = data['main']['feels_like']
                main_weather = data['weather'][0]['main']
                dt = data['dt']
                
                print(f"Data for {city} - Temp: {temp}°C, Feels Like: {feels_like}°C, Weather: {main_weather}, Time: {dt}")
                
                # Insert the weather data into the database
                cursor.execute(''' 
                    INSERT INTO weather (city, temperature, feels_like, weather_condition, timestamp)
                    VALUES (?, ?, ?, ?, ?)
                ''', (city, temp, feels_like, main_weather, dt))
                conn.commit()
            else:
                print(f"Failed to retrieve data for {city}: {data['message']}")

        except Exception as e:
            print(f"An error occurred while fetching data for {city}: {str(e)}")

    conn.close()

# Create the weather table
create_table()


schedule.every(5).minutes.do(fetch_weather_data)

if __name__ == "__main__":
    print("Starting weather data fetcher...")
    fetch_weather_data()
    while True:
        schedule.run_pending()
        time.sleep(1)
