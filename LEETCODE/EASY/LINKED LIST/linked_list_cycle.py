"""
Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle if some node can be reached again by continuously following the next pointer.
Return true if there is a cycle, otherwise return false.

Example 1:
    Input : head = [3, 2, 0, -4], pos = 1  (tail connects to index 1)
    Output: True

Example 2:
    Input : head = [1, 2], pos = 0
    Output: True

Example 3:
    Input : head = [1], pos = -1
    Output: False

Constraints:
    - The number of nodes is in the range [0, 10^4]

Time Complexity  : O(n)
Space Complexity : O(1)
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


try:
    raw = input("ENTER LINKED LIST VALUES (space separated)\n")
    values = list(map(int, raw.split()))

    if not values:
        raise ValueError("Input cannot be empty.")

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    pos = int(input("ENTER CYCLE POSITION (-1 for no cycle)\n"))
    if 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]

    print(f"HAS CYCLE: {has_cycle(nodes[0])}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
