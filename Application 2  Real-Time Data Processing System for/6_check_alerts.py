ALERT_THRESHOLD_TEMP = 35.0  # User-configurable threshold for temperature

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
