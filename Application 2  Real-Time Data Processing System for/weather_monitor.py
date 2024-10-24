import requests
import time
from datetime import datetime
import psycopg2
import matplotlib.pyplot as plt

# API Key and City List
API_KEY = '0df472a1c4ab65341b538215d9efc4c7'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

# PostgreSQL Connection
conn = psycopg2.connect(
    host="db",  # The hostname matches the service name in docker-compose.yml
    database="weather_db",
    user="my_user_id",
    password="password"
)
cur = conn.cursor()

# Create table for weather data
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            city VARCHAR(50),
            temperature FLOAT,
            feels_like FLOAT,
            main VARCHAR(50),
            dt TIMESTAMP
        )
    """)
    conn.commit()

# Fetch weather data for a specific city
def get_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': api_key}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Temperature conversion from Kelvin to Celsius/Fahrenheit
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(kelvin, unit="C"):
    if unit == "C":
        return kelvin_to_celsius(kelvin)
    elif unit == "F":
        return kelvin_to_fahrenheit(kelvin)
    else:
        return kelvin  # return Kelvin by default

# Insert weather data into PostgreSQL
def insert_weather_data(city, temperature, feels_like, main, dt):
    cur.execute("""
        INSERT INTO weather_data (city, temperature, feels_like, main, dt)
        VALUES (%s, %s, %s, %s, %s)
    """, (city, temperature, feels_like, main, dt))
    conn.commit()

# Process the weather data and store it in the database
def process_weather_data(data, unit="C"):
    city = data['name']
    temp = convert_temperature(data['main']['temp'], unit)
    feels_like = convert_temperature(data['main']['feels_like'], unit)
    main_weather = data['weather'][0]['main']
    timestamp = datetime.fromtimestamp(data['dt'])

    insert_weather_data(city, temp, feels_like, main_weather, timestamp)

# Calculate daily summaries (average, max, min, dominant weather)
def calculate_daily_summary():
    cur.execute("""
        SELECT city, 
               DATE(dt) as day, 
               AVG(temperature), 
               MAX(temperature), 
               MIN(temperature), 
               mode() WITHIN GROUP (ORDER BY main) as dominant_weather
        FROM weather_data
        GROUP BY city, day
    """)
    summaries = cur.fetchall()
    return summaries

# Alert if temperature exceeds threshold for two consecutive updates
ALERT_THRESHOLD_TEMP = 35.0

def check_alerts(city, current_temp):
    cur.execute("""
        SELECT temperature 
        FROM weather_data 
        WHERE city=%s 
        ORDER BY dt DESC 
        LIMIT 2
    """, (city,))
    temps = cur.fetchall()

    if len(temps) == 2 and all(temp[0] > ALERT_THRESHOLD_TEMP for temp in temps):
        print(f"ALERT: {city} temperature has exceeded {ALERT_THRESHOLD_TEMP}°C for 2 consecutive updates.")

# Plot temperature trend
def plot_temperature_trend(city):
    cur.execute("""
        SELECT dt, temperature 
        FROM weather_data 
        WHERE city=%s 
        ORDER BY dt
    """, (city,))
    data = cur.fetchall()
    timestamps, temps = zip(*data)
    
    plt.plot(timestamps, temps, label=f"Temperature in {city}")
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title(f"Temperature Trend for {city}")
    plt.legend()
    plt.show()

# Main function to run the real-time monitoring system
def run_weather_monitoring():
    create_table()

    # Loop to fetch and process weather data every 5 minutes
    while True:
        for city in CITIES:
            weather_data = get_weather_data(city, API_KEY)
            if weather_data:
                process_weather_data(weather_data)
                check_alerts(city, weather_data['main']['temp'])
        
        # Wait for 5 minutes before the next update
        time.sleep(300)

        # Display daily summaries (Optional for testing)
        summaries = calculate_daily_summary()
        for summary in summaries:
            print(summary)

# Run the monitoring system
if __name__ == "__main__":
    run_weather_monitoring()
