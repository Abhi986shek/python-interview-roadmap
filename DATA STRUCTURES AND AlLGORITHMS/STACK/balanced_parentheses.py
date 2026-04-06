"""
Balanced Parentheses using Stack

Check if an expression has properly matched brackets.
For every closing bracket, the top of the stack must hold its matching opener.

Time Complexity  : O(n)
Space Complexity : O(n)
"""


def is_balanced(expr):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expr:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


try:
    expr = input("ENTER THE EXPRESSION\n")

    if not expr.strip():
        raise ValueError("Expression cannot be empty.")

    if is_balanced(expr):
        print("BRACKETS ARE BALANCED")
    else:
        print("BRACKETS ARE NOT BALANCED")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
