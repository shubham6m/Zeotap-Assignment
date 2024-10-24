import re

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
