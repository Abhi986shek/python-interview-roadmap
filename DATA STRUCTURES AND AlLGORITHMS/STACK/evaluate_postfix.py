"""
Evaluate a Postfix Expression

In postfix notation, operators come after their operands.
Use a stack — push operands, and when an operator is found,
pop two operands, apply the operator, push the result back.

Example:
Input : "2 3 + 4 *"
Output: 20  (because (2+3)*4 = 20)

Time Complexity  : O(n)
Space Complexity : O(n)
"""


def evaluate_postfix(expr):
    stack = []
    tokens = expr.split()

    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        elif token in ('+', '-', '*', '/'):
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression.")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Division by zero.")
                stack.append(int(a / b))
        else:
            raise ValueError(f"Unknown token '{token}' in expression.")

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression.")

    return stack[0]


try:
    expr = input("ENTER THE POSTFIX EXPRESSION (space separated tokens)\n")

    if not expr.strip():
        raise ValueError("Expression cannot be empty.")

    result = evaluate_postfix(expr)
    print(f"RESULT: {result}")

except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
