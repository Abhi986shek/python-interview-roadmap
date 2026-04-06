"""
Module: balanced_brackets.py
Description: Checks whether an expression has properly balanced brackets, parentheses, and braces.
Logic: Uses a stack to track opening brackets. For each closing bracket, verifies
the top of the stack holds the matching opener. Returns True only if the stack is empty at the end.
"""
def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack

try:
    expr = input("ENTER THE EXPRESSION\n")
    if not expr.strip():
        raise ValueError("Input cannot be empty.")
    print("Balanced" if is_balanced(expr) else "Not Balanced")
except Exception as e:
    print(f"Error: {e}")