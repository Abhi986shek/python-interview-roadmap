"""
Middle of the Linked List

Given the head of a singly linked list, return the middle node.
If there are two middle nodes, return the second middle node.

Example 1:
    Input : head = [1, 2, 3, 4, 5]
    Output: [3, 4, 5]  (node with value 3)

Example 2:
    Input : head = [1, 2, 3, 4, 5, 6]
    Output: [4, 5, 6]  (node with value 4, the second middle)

Constraints:
    - The number of nodes in the list is in the range [1, 100]

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


def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


try:
    raw = input("ENTER LINKED LIST VALUES (space separated)\n")
    values = list(map(int, raw.split()))

    if not values:
        raise ValueError("Input cannot be empty.")

    head = build(values)
    mid = middle_node(head)
    print(f"MIDDLE NODE ONWARDS: {to_list(mid)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
