"""
Reverse a Linked List

Reverse the order of nodes in a singly linked list.

Approaches:
    Iterative  : O(n) time, O(1) space
    Recursive  : O(n) time, O(n) space (call stack)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_list(values):
    head = None
    for val in reversed(values):
        node = Node(val)
        node.next = head
        head = node
    return head


def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(elements) + " -> None")


def reverse_iterative(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def reverse_recursive(head):
    if not head or not head.next:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


try:
    raw = input("ENTER THE LINKED LIST ELEMENTS (space separated)\n")
    values = list(map(int, raw.split()))

    if not values:
        raise ValueError("Input cannot be empty.")

    choice = input("USE ITERATIVE OR RECURSIVE? (i/r)\n").strip().lower()

    head = build_list(values)
    print("ORIGINAL LIST: ", end="")
    display(head)

    if choice == 'r':
        head = reverse_recursive(head)
    else:
        head = reverse_iterative(head)

    print("REVERSED LIST: ", end="")
    display(head)

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
