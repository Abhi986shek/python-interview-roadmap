"""
Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Example 1:
    Input : root = [1, 2, 2, 3, 4, 4, 3]
    Output: True

Example 2:
    Input : root = [1, 2, 2, null, 3, null, 3]
    Output: False

Constraints:
    - The number of nodes is in the range [1, 1000]

Time Complexity  : O(n)
Space Complexity : O(n)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def is_symmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))
    return is_mirror(root.left, root.right)


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

    if not values:
        raise ValueError("Input cannot be empty.")

    root = build(values)
    print(f"IS SYMMETRIC: {is_symmetric(root)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
