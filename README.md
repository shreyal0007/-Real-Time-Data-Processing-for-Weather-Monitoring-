## Objective
The Real-Time Weather Monitoring System aims to monitor weather conditions and provide summarized insights using rollups and aggregates. The system continuously retrieves data from the OpenWeatherMap API and analyzes it for key weather parameters.

## Data Source
The system utilizes the OpenWeatherMap API. To access the data, you will need to sign up for a free API key [here](https://openweathermap.org/).

### Key Weather Parameters:
- **main**: Main weather condition (e.g., Rain, Snow, Clear)
- **temp**: Current temperature in Celsius
- **feels_like**: Perceived temperature in Celsius
- **dt**: Time of the data update (Unix timestamp)

## Features
1. **Continuous Data Retrieval**: The system fetches real-time weather data at configurable intervals (e.g., every 5 minutes) for major Indian metros: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
2. **Daily Weather Summary**: 
   - Calculates daily aggregates: average temperature, maximum temperature, minimum temperature, and dominant weather condition.
3. **Alerting Thresholds**: 
   - User-configurable thresholds for temperature alerts.
   - Triggers alerts if conditions exceed specified thresholds.
4. **Data Visualization**: 
   - Displays daily weather summaries and historical trends using graphs.

## Project Structure
The project consists of the following Python files:

- **`fetchweather.py`**: Fetches weather data and stores it in a local SQLite database after every 5 minutes.
- **`displaydata.py`**: Displays the data stored in the SQLite database.
- **`visualize_weather.py`**: Generates line graphs to show weather trends for all five cities.
- **`weather_summary.py`**: Summarizes the fetched weather data from all locations.
- **`weather_alert.py`**: Checks if the temperature exceeds 35°C and triggers an alert.

## Prerequisites
- Python 3.x
- SQLite (comes pre-installed with Python)
- An OpenWeatherMap API key


# Setup and Usage Instructions

Follow these steps in order to set up the project:

1. **Clone the Repository**:
   - Clone the repository to your local machine.

2. **Install Dependencies**:
   - Run `pip install -r requirements.txt` in your terminal.

3. **Fetch Weather Data**:
   - Start by running the `fetchweather.py` file to begin fetching real-time data.
   - Command: `python fetchweather.py`

4. **Display Stored Data**:
   - After fetching the data, run the `displaydata.py` file to see the data stored in the database.
   - Command: `python displaydata.py`

5. **Generate Weather Summary**:
   - Run the `weather_summary.py` file to get a summary of the fetched data.
   - Command: `python weather_summary.py`

6. **Check Alerts**:
   - Execute the `weather_alert.py` file to check for any temperature alerts.
   - Command: `python weather_alert.py`

7. **Visualize Weather Trends**:
   - Finally, run the `visualize_weather.py` file to visualize the weather trends.
   - Command: `python visualize_weather.py`


# Future Improvements for Real-Time Weather Monitoring System

## 1. Simultaneous Running
- **Description**: Modify the system to allow `fetchweather.py` to run simultaneously in the background while executing other scripts. This will enable continuous data fetching without stopping the execution of other functionalities.
- **Benefit**: Enhances user experience by ensuring real-time data availability for analysis, alerts, and visualizations without interruption.

## 2. Enhanced Data Storage
- **Description**: Consider using a more robust database solution like PostgreSQL or MongoDB for better data management and scalability.
- **Benefit**: Improved data integrity, performance, and scalability, allowing the system to handle larger datasets and more complex queries.

## 3. User Interface
- **Description**: Develop a user-friendly interface to interact with the system, visualize data, and configure settings more easily.
- **Benefit**: Streamlines user interaction, making it more accessible for users without technical expertise to manage and interpret weather data effectively.

## Contact
For any queries or suggestions, feel free to contact:
- **Name**: Shreyal Jain
- **Email**: shreyaljain0007@gmail.com
