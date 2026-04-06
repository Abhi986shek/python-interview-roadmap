"""
Check if a Binary Tree is Height Balanced

A tree is balanced if for every node, the height difference between
its left and right subtrees is at most 1.

Time Complexity  : O(n)
Space Complexity : O(n)
"""

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if not root:
        return Node(data)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if not node.left:
            node.left = Node(data)
            return root
        queue.append(node.left)
        if not node.right:
            node.right = Node(data)
            return root
        queue.append(node.right)
    return root


def check_balanced(node):
    # returns -1 if unbalanced, otherwise returns height
    if not node:
        return 0

    left = check_balanced(node.left)
    if left == -1:
        return -1

    right = check_balanced(node.right)
    if right == -1:
        return -1

    if abs(left - right) > 1:
        return -1

    return 1 + max(left, right)


try:
    raw = input("ENTER TREE ELEMENTS (space separated, inserted level by level)\n")
    values = list(map(int, raw.split()))

    if not values:
        raise ValueError("Input cannot be empty.")

    root = None
    for val in values:
        root = insert(root, val)

    if check_balanced(root) != -1:
        print("THE TREE IS BALANCED")
    else:
        print("THE TREE IS NOT BALANCED")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
