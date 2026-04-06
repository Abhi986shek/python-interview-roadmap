"""
Remove Nth Node from the End of a Linked List

Uses two pointers separated by n steps.
When the fast pointer reaches the end, slow is just before the target node.

Time Complexity  : O(n) - single pass
Space Complexity : O(1)
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


def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = slow = dummy

    # move fast n+1 steps ahead
    for _ in range(n + 1):
        if not fast:
            raise ValueError(f"N={n} is greater than the length of the list.")
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next


try:
    raw = input("ENTER THE LINKED LIST ELEMENTS (space separated)\n")
    values = list(map(int, raw.split()))

    if not values:
        raise ValueError("Input cannot be empty.")

    n = int(input("ENTER N (remove nth node from end)\n"))

    if n <= 0:
        raise ValueError("N must be greater than 0.")

    head = build_list(values)

    print("ORIGINAL LIST: ", end="")
    display(head)

    head = remove_nth_from_end(head, n)

    print("LIST AFTER REMOVAL: ", end="")
    display(head)

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
