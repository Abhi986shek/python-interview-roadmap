"""
You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:
Input: root = [0,0,null,0,0]
Output: 1

Example 2:
Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- Node.val == 0
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_camera_cover(root):
    cameras = 0
    
    def dfs(node):
        nonlocal cameras
        if not node:
            return 2
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        if left == 0 or right == 0:
            cameras += 1
            return 1
        
        if left == 1 or right == 1:
            return 2
        
        return 0
    
    return cameras + (1 if dfs(root) == 0 else 0)

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
    print(f"MIN CAMERAS: {min_camera_cover(root)}")
except Exception as e:
    print(f"An error occurred: {e}")
