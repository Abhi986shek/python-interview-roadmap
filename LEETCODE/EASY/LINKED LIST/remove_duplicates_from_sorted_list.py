"""
Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that
each element appears only once. Return the linked list sorted as well.

Example 1:
    Input : head = [1, 1, 2]
    Output: [1, 2]

Example 2:
    Input : head = [1, 1, 2, 3, 3]
    Output: [1, 2, 3]

Constraints:
    - The number of nodes is in the range [0, 300]
    - The list is sorted in ascending order

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


def delete_duplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


try:
    raw = input("ENTER SORTED LINKED LIST VALUES (space separated)\n")
    values = list(map(int, raw.split()))

    if not values:
        raise ValueError("Input cannot be empty.")

    head = build(values)
    result = delete_duplicates(head)
    print(f"AFTER REMOVING DUPLICATES: {to_list(result)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
