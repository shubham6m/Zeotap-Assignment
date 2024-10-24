def combine_rules(rules, operator='AND'):
    ast_list = [create_rule(rule) for rule in rules]
    while len(ast_list) > 1:
        left = ast_list.pop(0)
        right = ast_list.pop(0)
        combined_ast = Node("operator", left, right, operator)
        ast_list.append(combined_ast)
    return ast_list[0]
