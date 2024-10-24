import matplotlib.pyplot as plt

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

# Plotting temperature trend for Delhi
plot_temperature_trend('Delhi')
