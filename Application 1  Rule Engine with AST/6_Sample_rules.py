# Sample rules
rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"

# Create individual ASTs for the rules
ast1 = create_rule(rule1)
ast2 = create_rule(rule2)

# Combine the rules using AND operator
combined_rule_ast = combine_rules([rule1, rule2], operator="AND")

# Example user data
user_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

# Evaluate the rule against user data
result = evaluate_rule(combined_rule_ast, user_data)
print("User is eligible:", result)
