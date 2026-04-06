"""
Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
    Input : root = [4, 2, 7, 1, 3, 6, 9]
    Output: [4, 7, 2, 9, 6, 3, 1]

Example 2:
    Input : root = [2, 1, 3]
    Output: [2, 3, 1]

Constraints:
    - The number of nodes is in the range [0, 100]

Time Complexity  : O(n)
Space Complexity : O(n)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def build(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return result


try:
    raw = input("ENTER TREE VALUES LEVEL ORDER (space separated, use 0 for null)\n")
    values = [int(x) if x != '0' else None for x in raw.split()]

    if not values:
        raise ValueError("Input cannot be empty.")

    root = build(values)
    inverted = invert_tree(root)
    print(f"INVERTED TREE (LEVEL ORDER): {level_order(inverted)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
