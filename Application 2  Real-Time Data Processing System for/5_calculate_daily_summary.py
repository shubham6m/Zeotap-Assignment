def calculate_daily_summary():
    # Group by city and date
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

# Example of how to fetch summaries
daily_summaries = calculate_daily_summary()
for summary in daily_summaries:
    print(summary)
