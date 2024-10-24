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
