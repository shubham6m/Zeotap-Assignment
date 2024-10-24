import re
import sqlite3

# Define the AST node structure
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" for AND/OR or "operand" for conditions
        self.left = left  # Left child node (for operators)
        self.right = right  # Right child node (for operators)
        self.value = value  # Value for operand nodes (condition as string)

    def __repr__(self):
        if self.type == "operand":
            return f"Operand({self.value})"
        elif self.type == "operator":
            return f"Operator({self.left} {self.value} {self.right})"

    # Evaluate the node based on the data provided
    def evaluate(self, data):
        if self.type == "operand":
            return eval(self.value, {}, data)
        elif self.type == "operator":
            if self.value == "AND":
                return self.left.evaluate(data) and self.right.evaluate(data)
            elif self.value == "OR":
                return self.left.evaluate(data) or self.right.evaluate(data)
        return False


# Function to create rule (AST) from a rule string
def create_rule(rule_string):
    # Remove extra spaces and tokenize the rule string based on parentheses and operators
    tokens = re.findall(r'\w+|[><=()]|\band\b|\bor\b', rule_string)
    return parse_expression(tokens)

# Helper function to parse a tokenized expression into AST
def parse_expression(tokens):
    stack = []
    while tokens:
        token = tokens.pop(0)
        if token == '(':
            stack.append(token)
        elif token == ')':
            right = stack.pop()
            operator = stack.pop()
            left = stack.pop()
            stack.pop()  # pop '('
            stack.append(Node("operator", left, right, operator))
        elif token.lower() in ['and', 'or']:
            operator = token.upper()
            stack.append(operator)
        else:
            condition = token
            if tokens and tokens[0] in ['>', '<', '=']:
                condition += tokens.pop(0) + tokens.pop(0)  # Construct conditions like age > 30
            stack.append(Node("operand", value=condition))
    return stack[0] if stack else None


# Function to combine multiple rules into a single AST
def combine_rules(rules, operator='AND'):
    ast_list = [create_rule(rule) for rule in rules]
    while len(ast_list) > 1:
        left = ast_list.pop(0)
        right = ast_list.pop(0)
        combined_ast = Node("operator", left, right, operator)
        ast_list.append(combined_ast)
    return ast_list[0]


# Function to evaluate a rule (AST) against user data
def evaluate_rule(ast, data):
    return ast.evaluate(data)


# Database Functions: Connecting to SQLite to store rules
def init_db():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_string TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to save rule to the database
def save_rule(rule_string, description):
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rules (rule_string, description) VALUES (?, ?)", (rule_string, description))
    conn.commit()
    conn.close()

# Function to retrieve rules from the database
def get_rules():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rules")
    rules = cursor.fetchall()
    conn.close()
    return rules

# Modify existing rule (Bonus feature)
def modify_rule(ast, new_value):
    if ast.type == "operand":
        ast.value = new_value
    return ast

# Test Cases
def test_create_rule():
    rule_string = "age > 30 AND salary > 50000"
    ast = create_rule(rule_string)
    assert ast.type == "operator"
    assert ast.left.value == "age > 30"
    assert ast.right.value == "salary > 50000"

def test_combine_rules():
    rule1 = "age > 30 AND salary > 50000"
    rule2 = "experience > 5 OR department = 'Sales'"
    combined_ast = combine_rules([rule1, rule2], "AND")
    assert combined_ast.type == "operator"

def test_evaluate_rule():
    rule_string = "age > 30 AND salary > 50000"
    ast = create_rule(rule_string)
    user_data = {"age": 35, "salary": 60000}
    assert evaluate_rule(ast, user_data) == True

    user_data = {"age": 25, "salary": 40000}
    assert evaluate_rule(ast, user_data) == False

# Running Tests
if __name__ == '__main__':
    init_db()

    # Test the system by creating, saving, and evaluating rules
    print("Running unit tests...")
    test_create_rule()
    test_combine_rules()
    test_evaluate_rule()
    print("All tests passed.")

    # Sample rules
    rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"

    # Create individual ASTs for the rules
    ast1 = create_rule(rule1)
    ast2 = create_rule(rule2)

    # Combine the rules using AND operator
    combined_rule_ast = combine_rules([rule1, rule2], operator="AND")

    # Save rule to the database
    save_rule(rule1, "Rule 1 for Sales and Marketing")
    save_rule(rule2, "Rule 2 for Marketing")

    # Retrieve and print saved rules
    rules = get_rules()
    print("Saved rules in the database:")
    for rule in rules:
        print(rule)

    # Example user data
    user_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

    # Evaluate the rule against user data
    result = evaluate_rule(combined_rule_ast, user_data)
    print("User is eligible:", result)

    # Modify a rule (optional)
    modified_ast = modify_rule(ast1, "age > 25")
    result = evaluate_rule(modified_ast, user_data)
    print("Modified rule eligibility:", result)
