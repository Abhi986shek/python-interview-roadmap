"""
Merge Two Sorted Linked Lists

Merges two sorted linked lists into one sorted linked list.
Done in-place without using extra space.

Time Complexity  : O(n + m) - where n and m are lengths of the two lists
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


def merge_sorted(l1, l2):
    dummy = Node(0)
    curr = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 if l1 else l2
    return dummy.next


try:
    raw1 = input("ENTER FIRST SORTED LIST ELEMENTS (space separated)\n")
    raw2 = input("ENTER SECOND SORTED LIST ELEMENTS (space separated)\n")

    vals1 = list(map(int, raw1.split()))
    vals2 = list(map(int, raw2.split()))

    if not vals1 or not vals2:
        raise ValueError("Both lists must have at least one element.")

    l1 = build_list(vals1)
    l2 = build_list(vals2)

    merged = merge_sorted(l1, l2)

    print("MERGED SORTED LIST: ", end="")
    display(merged)

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
