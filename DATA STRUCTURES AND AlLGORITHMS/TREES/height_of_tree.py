"""
Height of a Binary Tree

The height is the number of edges on the longest path from root to a leaf.
Calculated recursively — height = 1 + max(left height, right height).

Example:
        1
       / \
      2   3
     / \
    4   5
Height = 2

Time Complexity  : O(n)
Space Complexity : O(n) - recursive call stack
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


def height(node):
    if not node:
        return -1  # -1 so a single node tree has height 0
    return 1 + max(height(node.left), height(node.right))


try:
    raw = input("ENTER TREE ELEMENTS (space separated, inserted level by level)\n")
    values = list(map(int, raw.split()))

    if not values:
        raise ValueError("Input cannot be empty.")

    root = None
    for val in values:
        root = insert(root, val)

    print(f"HEIGHT OF THE TREE: {height(root)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
