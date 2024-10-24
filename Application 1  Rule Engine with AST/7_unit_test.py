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

# Run tests
test_create_rule()
test_combine_rules()
test_evaluate_rule()
print("All tests passed.")
