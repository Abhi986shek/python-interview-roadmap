"""
Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example 1:
    Input : root = [3, 9, 20, null, null, 15, 7]
    Output: 3

Example 2:
    Input : root = [1, null, 2]
    Output: 2

Constraints:
    - The number of nodes is in the range [0, 10^4]

Time Complexity  : O(n)
Space Complexity : O(n)
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def build(values):
    if not values:
        return None
    from collections import deque
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


try:
    raw = input("ENTER TREE VALUES LEVEL ORDER (space separated, use 0 for null)\n")
    values = [int(x) if x != '0' else None for x in raw.split()]

    if not values:
        raise ValueError("Input cannot be empty.")

    root = build(values)
    print(f"MAXIMUM DEPTH: {max_depth(root)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
