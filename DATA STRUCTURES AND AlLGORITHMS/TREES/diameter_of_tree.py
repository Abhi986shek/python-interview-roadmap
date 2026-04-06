"""
Diameter of a Binary Tree

The diameter is the length of the longest path between any two nodes.
The path may or may not pass through the root.
At each node, diameter = left height + right height + 2.

Example:
        1
       / \
      2   3
     / \
    4   5
Diameter = 3 (path: 4 -> 2 -> 1 -> 3  or  5 -> 2 -> 1 -> 3)

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


def diameter(node, result):
    if not node:
        return -1
    left_h = diameter(node.left, result)
    right_h = diameter(node.right, result)
    result[0] = max(result[0], left_h + right_h + 2)
    return 1 + max(left_h, right_h)


try:
    raw = input("ENTER TREE ELEMENTS (space separated, inserted level by level)\n")
    values = list(map(int, raw.split()))

    if not values:
        raise ValueError("Input cannot be empty.")

    root = None
    for val in values:
        root = insert(root, val)

    result = [0]
    diameter(root, result)
    print(f"DIAMETER OF THE TREE: {result[0]}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
