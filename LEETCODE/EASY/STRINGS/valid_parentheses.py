"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input : s = "()"
    Output: True

Example 2:
    Input : s = "()[]{}"
    Output: True

Example 3:
    Input : s = "(]"
    Output: False

Constraints:
    - 1 <= s.length <= 10^4
    - s consists of parentheses only

Time Complexity  : O(n)
Space Complexity : O(n)
"""


def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in "({[":
            stack.append(c)
        elif not stack or stack[-1] != pairs[c]:
            return False
        else:
            stack.pop()
    return len(stack) == 0


try:
    s = input("ENTER THE EXPRESSION\n")
    if not s:
        raise ValueError("Input cannot be empty.")

    print(f"IS VALID: {is_valid(s)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
