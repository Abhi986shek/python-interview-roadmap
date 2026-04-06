"""
Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Input : head = [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]

Example 2:
    Input : head = [1, 2]
    Output: [2, 1]

Constraints:
    - The number of nodes in the list is in the range [0, 5000]

Time Complexity  : O(n)
Space Complexity : O(1)
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def build(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


try:
    raw = input("ENTER LINKED LIST VALUES (space separated)\n")
    values = list(map(int, raw.split()))

    if not values:
        raise ValueError("Input cannot be empty.")

    head = build(values)
    reversed_head = reverse_list(head)
    print(f"REVERSED: {to_list(reversed_head)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
