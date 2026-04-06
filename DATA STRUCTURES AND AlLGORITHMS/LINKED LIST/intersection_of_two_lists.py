"""
Intersection of Two Linked Lists

Find the node where two linked lists meet.
Uses the two-pointer trick — when one pointer reaches the end,
redirect it to the head of the other list. They meet at the intersection.

Time Complexity  : O(n + m)
Space Complexity : O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_intersection(head1, head2):
    a, b = head1, head2
    while a != b:
        a = a.next if a else head2
        b = b.next if b else head1
    return a


try:
    raw1 = input("ENTER FIRST LIST ELEMENTS (space separated)\n")
    raw2 = input("ENTER SECOND LIST ELEMENTS (space separated)\n")
    raw_common = input("ENTER COMMON TAIL ELEMENTS (space separated, or leave empty)\n")

    vals1 = list(map(int, raw1.split()))
    vals2 = list(map(int, raw2.split()))
    vals_common = list(map(int, raw_common.split())) if raw_common.strip() else []

    # build common tail
    common_head = None
    for val in reversed(vals_common):
        node = Node(val)
        node.next = common_head
        common_head = node

    # build list 1
    head1 = None
    for val in reversed(vals1):
        node = Node(val)
        node.next = head1
        head1 = node
    # attach common tail to list 1
    if head1:
        curr = head1
        while curr.next:
            curr = curr.next
        curr.next = common_head
    else:
        head1 = common_head

    # build list 2
    head2 = None
    for val in reversed(vals2):
        node = Node(val)
        node.next = head2
        head2 = node
    # attach same common tail to list 2
    if head2:
        curr = head2
        while curr.next:
            curr = curr.next
        curr.next = common_head
    else:
        head2 = common_head

    result = find_intersection(head1, head2)

    if result:
        print(f"INTERSECTION NODE VALUE: {result.data}")
    else:
        print("NO INTERSECTION FOUND")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
