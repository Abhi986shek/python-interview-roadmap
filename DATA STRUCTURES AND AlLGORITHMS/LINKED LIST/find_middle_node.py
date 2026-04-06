"""
Find the Middle Node of a Linked List

Uses the slow/fast pointer technique.
Slow moves one step, fast moves two steps.
When fast reaches the end, slow is at the middle.

Time Complexity  : O(n)
Space Complexity : O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


try:
    raw = input("ENTER THE LINKED LIST ELEMENTS (space separated)\n")
    values = list(map(int, raw.split()))

    if not values:
        raise ValueError("Input cannot be empty.")

    # build list
    head = None
    for val in reversed(values):
        node = Node(val)
        node.next = head
        head = node

    middle = find_middle(head)
    print(f"MIDDLE NODE VALUE: {middle.data}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
