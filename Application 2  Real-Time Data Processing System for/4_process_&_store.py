import psycopg2
from datetime import datetime

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="weather_db",
    user="my_user_id",
    password="password"
)
cur = conn.cursor()

# Initialize a table for weather data
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

# Function to insert weather data into the database
def insert_weather_data(city, temperature, feels_like, main, dt):
    cur.execute("""
        INSERT INTO weather_data (city, temperature, feels_like, main, dt)
        VALUES (%s, %s, %s, %s, %s)
    """, (city, temperature, feels_like, main, dt))
    conn.commit()

# Processing data for a city
def process_weather_data(data, unit="C"):
    city = data['name']
    temp = convert_temperature(data['main']['temp'], unit)
    feels_like = convert_temperature(data['main']['feels_like'], unit)
    main_weather = data['weather'][0]['main']
    timestamp = datetime.fromtimestamp(data['dt'])
    
    # Insert processed data into DB
    insert_weather_data(city, temp, feels_like, main_weather, timestamp)
