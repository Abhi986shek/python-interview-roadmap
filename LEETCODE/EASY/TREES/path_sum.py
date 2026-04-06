"""
Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree
has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
    Input : root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], targetSum = 22
    Output: True  (path: 5 -> 4 -> 11 -> 2)

Example 2:
    Input : root = [1, 2, 3], targetSum = 5
    Output: False

Constraints:
    - The number of nodes is in the range [0, 5000]

Time Complexity  : O(n)
Space Complexity : O(n)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def has_path_sum(root, target):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target
    return (has_path_sum(root.left, target - root.val) or
            has_path_sum(root.right, target - root.val))


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


try:
    raw = input("ENTER TREE VALUES LEVEL ORDER (space separated, use 0 for null)\n")
    values = [int(x) if x != '0' else None for x in raw.split()]
    target = int(input("ENTER TARGET SUM\n"))

    root = build(values)
    print(f"HAS PATH SUM {target}: {has_path_sum(root, target)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
