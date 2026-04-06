"""
Sort a Stack

Sort a stack in ascending order (smallest on top) using recursion.
No extra data structure allowed — only the call stack.

Time Complexity  : O(n²)
Space Complexity : O(n) - recursive call stack
"""


def insert_in_sorted_order(stack, val):
    # base case: empty stack or val is smaller than top
    if not stack or stack[-1] <= val:
        stack.append(val)
        return

    top = stack.pop()
    insert_in_sorted_order(stack, val)
    stack.append(top)


def sort_stack(stack):
    if not stack:
        return

    top = stack.pop()
    sort_stack(stack)
    insert_in_sorted_order(stack, top)


try:
    raw = input("ENTER THE STACK ELEMENTS (space separated, first = bottom)\n")
    elements = list(map(int, raw.split()))

    if not elements:
        raise ValueError("Stack cannot be empty.")

    stack = elements[:]
    print(f"ORIGINAL STACK (top -> bottom): {stack[::-1]}")

    sort_stack(stack)
    print(f"SORTED STACK (smallest on top): {stack[::-1]}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
