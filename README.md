# Zeotap-Assignment

Here’s the `README.md` file,
**Rule Engine with AST** project. It includes all the necessary details for building, running, and understanding the project:

**NOTE : All file are exist in repo but only main file is run correctly other's are not because I will not import (link) one file to another to just decrease the complexity & understandibility of each code steps  please run "rule_engine.py" file** to run the application.

---

# Rule Engine with Abstract Syntax Tree (AST)

## Overview
This project is a simple rule engine system that uses an Abstract Syntax Tree (AST) to evaluate user eligibility based on certain attributes (e.g., age, department, salary, experience). The engine allows dynamic creation, combination, modification, and evaluation of rules, supporting conditions like AND/OR operators.

The system stores rules in a database, allowing for persistence and modification of the rules.

## Features
- **Create rules**: Convert a string rule into an AST.
- **Combine rules**: Combine multiple rules into a single AST with logical operators (`AND`, `OR`).
- **Evaluate rules**: Evaluate a rule or combined rules against a set of user data.
- **Modify rules**: Update existing rules for new conditions.
- **Database integration**: Store and retrieve rules using SQLite.
- **Unit testing**: Basic test cases for rule creation, combination, and evaluation.

### Sample Rules
- Rule 1: 
    ```((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)```
- Rule 2: 
    ```((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)```

## Prerequisites

- Python 3.x
- SQLite3 (SQLite will automatically initialize with Python's standard library)

## How to Install and Run

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/rule-engine-ast.git
    cd rule-engine-ast
    ```

2. **Set up a virtual environment (optional but recommended)**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```

3. **Install dependencies**:
    There are no external dependencies, but if you want to extend the project, you can install required libraries by adding them to `requirements.txt`. For now, the code only uses the Python standard library.

4. **Run the application**:
    ```bash
    python rule_engine.py
    ```

## Project Structure

```
.
├── rule_engine.py    # Main Python file with all functionality
├── rules.db          # SQLite database file (auto-generated on first run)
├── README.md         # This file
```

### Key Components

1. **`Node` Class**: Represents the AST structure, where each node can either be an operator (`AND`, `OR`) or an operand (e.g., `age > 30`).
2. **`create_rule` Function**: Parses a string rule into an AST.
3. **`combine_rules` Function**: Combines multiple ASTs into a single AST using an operator like `AND` or `OR`.
4. **`evaluate_rule` Function**: Evaluates a given AST against the provided user data (dictionary).
5. **Database Functions**: Connects to SQLite for saving and retrieving rules. Initializes the database with a simple schema for rules.

### Example Code Usage

#### Creating a Rule
```python
rule_string = "age > 30 AND salary > 50000"
ast = create_rule(rule_string)
print(ast)  # Displays the AST
```

#### Combining Rules
```python
rule1 = "age > 30 AND salary > 50000"
rule2 = "experience > 5 OR department = 'Sales'"
combined_ast = combine_rules([rule1, rule2], operator="AND")
print(combined_ast)  # Displays the combined AST
```

#### Evaluating a Rule
```python
user_data = {"age": 35, "salary": 60000, "experience": 3}
result = evaluate_rule(combined_ast, user_data)
print("User eligible:", result)  # Output: True or False
```

### Testing

Unit tests are included for basic rule creation, combination, and evaluation.

#### Running Tests
```bash
python rule_engine.py
```
All test cases are executed when running the script, and the results are printed to the console.

## Database

The system uses **SQLite** for storing rules. Upon first run, an `rules.db` file is created automatically with the following schema:

- **Table**: `rules`
    - `id`: INTEGER PRIMARY KEY (Auto-incremented)
    - `rule_string`: TEXT (Stores the rule string representation)
    - `description`: TEXT (Optional description for each rule)

### Example of Saving a Rule
```python
save_rule(rule1, "Rule 1 for Sales")
```

### Example of Retrieving Saved Rules
```python
rules = get_rules()
for rule in rules:
    print(rule)
```

## Modifying a Rule
The system also allows you to modify an existing rule by directly changing the condition at a node.

```python
modified_ast = modify_rule(ast1, "age > 25")
result = evaluate_rule(modified_ast, user_data)
print("Modified rule eligibility:", result)
```

## Contributions

Feel free to fork this project, create issues, or submit pull requests for improvements, bug fixes, or new features.


### Future Enhancements

- **User Interface**: Adding a web-based UI for creating and evaluating rules.
- **Custom Operators**: Support for more complex operators and nested conditions.
- **More Databases**: Integration with other databases like PostgreSQL or MySQL.
- **Enhanced Rule Editing**: Ability to add/remove conditions from existing rules.

---




**Application 2 : Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates**
---

# Real-Time Weather Monitoring System

## Overview
This project is a real-time weather monitoring system that retrieves weather data from the [OpenWeatherMap API](https://openweathermap.org/). The system processes weather data for multiple cities, stores daily summaries, and triggers alerts based on user-defined thresholds. It also includes options for visualizing weather trends and conditions.

The system supports periodic data fetching, rollups and aggregates (such as daily averages, minimum/maximum temperature), and customizable weather condition alerts.

## Features
- **Continuous Data Retrieval**: Fetches weather data at configurable intervals from OpenWeatherMap API for selected Indian cities (e.g., Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
- **Daily Summaries**: Calculates daily weather aggregates:
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Dominant weather condition
- **Temperature Conversion**: Converts temperatures from Kelvin to Celsius (and optionally Fahrenheit).
- **Alerting System**: Triggers alerts when user-configured thresholds (e.g., temperature exceeding 35°C) are crossed.
- **Visualization**: Generates visual summaries and trends of weather data.

## Prerequisites

- Python 3.x
- OpenWeatherMap API key (sign up for a free API key [here](https://home.openweathermap.org/users/sign_up))
- SQLite3 (optional but included in Python standard library)
- Optional: Flask (if you want to run a web server for API integration)

## How to Install and Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/weather-monitoring-system.git
cd weather-monitoring-system
```

### 2. Set Up a Virtual Environment (Optional)
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
Install necessary Python dependencies using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
Rename the `.env.example` file to `.env` and insert your OpenWeatherMap API key:
```bash
mv .env.example .env
```
Inside the `.env` file:
```
API_KEY=your_openweathermap_api_key
```

### 5. Run the Application
Start the application, which will begin fetching weather data and generating summaries:
```bash
python weather_monitor.py
```

## Project Structure

```bash
.
├── weather_monitor.py      # Main script for weather data retrieval and processing
├── 6_check_alerts.py       # Script handling alert logic
├── 4_process_&_store.py    # Handles SQLite database operations
├── 7_plot_temperature_trend.py       # Generates visualizations for weather trends and summaries
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment file for API key
├── weather.db              # SQLite database (auto-generated)
├── README.md               # This file
```

### Key Components

1. **Weather Data Fetching**: Retrieves weather data from the OpenWeatherMap API at specified intervals (default: every 5 minutes).
2. **Temperature Conversion**: Converts temperature data from Kelvin to Celsius, and optionally Fahrenheit.
3. **Daily Weather Rollups**: Aggregates the fetched weather data for daily summaries, calculating:
   - Average, maximum, minimum temperatures
   - Dominant weather condition
4. **Alert System**: Monitors temperature and weather conditions against user-defined thresholds and triggers alerts via the console or other notifications.
5. **Visualization**: Generates plots and trends of historical weather data.

### Configuration

The system supports multiple configuration options like the frequency of weather updates, alert thresholds, and more. These can be set directly in the `weather_monitor.py` or via environment variables.

### Example Weather API Response
```json
{
  "main": {
    "temp": 300.15,
    "feels_like": 302.15,
    "temp_min": 299.15,
    "temp_max": 301.15
  },
  "weather": [{
    "main": "Clear",
    "description": "clear sky"
  }],
  "dt": 1605182400
}
```

### Example Usage in Code

#### Fetching Weather Data
```python
from weather_monitor import fetch_weather_data

city = "Delhi"
weather_data = fetch_weather_data(city)
print(weather_data)
```

#### Evaluating Alerts
```python
from weather_alerts import check_alerts

city_data = {
    "temp": 36, 
    "weather_condition": "Clear"
}
alert_triggered = check_alerts(city_data, threshold_temp=35)
if alert_triggered:
    print("Alert: Temperature exceeded the threshold!")
```

#### Storing Daily Weather Summary
```python
from weather_db import store_weather_summary

city = "Mumbai"
weather_summary = {"avg_temp": 30, "max_temp": 34, "min_temp": 28, "dominant_condition": "Clear"}
store_weather_summary(city, weather_summary)
```

### Running Tests
The system includes basic tests for weather fetching, data processing, and alert triggering.

#### Running Unit Tests
```bash
python -m unittest test_weather_monitor.py
```

## Database Schema

The system uses **SQLite** for persistence. The database stores daily weather summaries and includes the following schema:

- **Table**: `weather_summaries`
    - `id`: INTEGER PRIMARY KEY
    - `city`: TEXT (name of the city)
    - `date`: TEXT (date in `YYYY-MM-DD` format)
    - `avg_temp`: REAL (average temperature in Celsius)
    - `max_temp`: REAL (maximum temperature in Celsius)
    - `min_temp`: REAL (minimum temperature in Celsius)
    - `dominant_condition`: TEXT (dominant weather condition)

Example of a weather summary:
```sql
INSERT INTO weather_summaries (city, date, avg_temp, max_temp, min_temp, dominant_condition)
VALUES ('Mumbai', '2024-10-19', 30.5, 34.2, 28.3, 'Clear');
```

## Visualizations

The system can generate visualizations to represent weather trends over time, using libraries like Matplotlib. The visualizations include:
- Daily temperature trends
- Weather condition distributions
- Alert occurrences over time

To generate and display the visualization:
```bash
python visualizations.py
```

## Alerts and Thresholds

You can set custom thresholds for triggering alerts. For example, to trigger an alert when the temperature exceeds 35°C for two consecutive updates, you can configure the following in `weather_alerts.py`:
```python
THRESHOLD_TEMP = 35
```

The system will log alerts in the console and can be extended to send email or push notifications.

## Future Enhancements
- **Support for additional weather parameters**: Add features for tracking humidity, wind speed, and other conditions.
- **Forecast integration**: Extend the system to include weather forecasts and predictive summaries.
- **Web Interface**: Create a web-based dashboard for real-time monitoring, alerting, and data visualization using Flask.
- **Improved Alerting**: Integrate email/SMS/notification services for more advanced alerting.

---

### Contributing
Feel free to fork this repository, create issues, or submit pull requests for improvements, bug fixes, or new features.

---

This `README.md` provides an overview of how to install, run, and use the real-time weather monitoring system.

