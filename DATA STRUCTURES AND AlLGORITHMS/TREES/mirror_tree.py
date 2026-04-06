"""
Mirror / Invert a Binary Tree

Swap the left and right children of every node recursively.
The result is the mirror image of the original tree.

Example:
    Original        Mirrored
        1               1
       / \             / \
      2   3           3   2
     / \               \ /
    4   5             5   4

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


def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def mirror(node):
    if not node:
        return
    node.left, node.right = node.right, node.left
    mirror(node.left)
    mirror(node.right)


try:
    raw = input("ENTER TREE ELEMENTS (space separated, inserted level by level)\n")
    values = list(map(int, raw.split()))

    if not values:
        raise ValueError("Input cannot be empty.")

    root = None
    for val in values:
        root = insert(root, val)

    print(f"ORIGINAL LEVEL ORDER : {level_order(root)}")

    mirror(root)

    print(f"MIRRORED LEVEL ORDER : {level_order(root)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
