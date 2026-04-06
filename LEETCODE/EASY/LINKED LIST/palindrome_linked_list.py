"""
Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome
or false otherwise.

Example 1:
    Input : head = [1, 2, 2, 1]
    Output: True

Example 2:
    Input : head = [1, 2]
    Output: False

Constraints:
    - The number of nodes is in the range [1, 10^5]

Time Complexity  : O(n)
Space Complexity : O(n)
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


def is_palindrome(head):
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    return vals == vals[::-1]


try:
    raw = input("ENTER LINKED LIST VALUES (space separated)\n")
    values = list(map(int, raw.split()))

    if not values:
        raise ValueError("Input cannot be empty.")

    head = build(values)
    print(f"IS PALINDROME: {is_palindrome(head)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
