"""
Detect Cycle in a Linked List (Floyd's Algorithm)

Uses two pointers — slow moves one step, fast moves two steps.
If they ever meet, a cycle exists.

Time Complexity  : O(n)
Space Complexity : O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


try:
    raw = input("ENTER THE LINKED LIST ELEMENTS (space separated)\n")
    values = list(map(int, raw.split()))

    if not values:
        raise ValueError("Input cannot be empty.")

    # build list
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # optionally create a cycle for testing
    cycle_input = input("CREATE A CYCLE? IF YES ENTER THE INDEX TO CONNECT TAIL TO (or -1 for no cycle)\n")
    cycle_pos = int(cycle_input)

    if cycle_pos >= 0 and cycle_pos < len(nodes):
        nodes[-1].next = nodes[cycle_pos]

    head = nodes[0]

    if detect_cycle(head):
        print("CYCLE DETECTED IN THE LINKED LIST")
    else:
        print("NO CYCLE FOUND IN THE LINKED LIST")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
