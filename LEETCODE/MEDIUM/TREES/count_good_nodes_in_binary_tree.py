"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4

Example 2:
Input: root = [3,3,null,4,2]
Output: 3

Example 3:
Input: root = [1]
Output: 1

Constraints:
- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is between [-10^4, 10^4].
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def good_nodes(root):
    def dfs(node, max_val):
        if not node:
            return 0
        count = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)
        count += dfs(node.left, max_val)
        count += dfs(node.right, max_val)
        return count
    return dfs(root, float('-inf'))

def build_tree(values):
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
    raw = input("ENTER TREE (space separated, 0 for null)\n")
    values = [int(x) if x != '0' else None for x in raw.split()]
    root = build_tree(values)
    print(f"GOOD NODES: {good_nodes(root)}")
except Exception as e:
    print(f"An error occurred: {e}")
