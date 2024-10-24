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




