def modify_rule(ast, new_value):
    if ast.type == "operand":
        ast.value = new_value
    return ast
