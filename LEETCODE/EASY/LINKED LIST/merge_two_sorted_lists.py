"""
Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list made by splicing together
the nodes of the first two lists. Return the head of the merged list.

Example 1:
    Input : list1 = [1, 2, 4], list2 = [1, 3, 4]
    Output: [1, 1, 2, 3, 4, 4]

Example 2:
    Input : list1 = [], list2 = []
    Output: []

Constraints:
    - The number of nodes in both lists is in the range [0, 50]
    - Both lists are sorted in non-decreasing order

Time Complexity  : O(n + m)
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


def merge_two_lists(l1, l2):
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next


try:
    raw1 = input("ENTER FIRST LIST VALUES (space separated)\n")
    raw2 = input("ENTER SECOND LIST VALUES (space separated)\n")

    l1 = build(list(map(int, raw1.split()))) if raw1.strip() else None
    l2 = build(list(map(int, raw2.split()))) if raw2.strip() else None

    result = merge_two_lists(l1, l2)
    print(f"MERGED LIST: {to_list(result)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
