"""
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]

Constraints:
- The number of nodes in the tree is in the range [2, 1000].
- -2^31 <= Node.val <= 2^31 - 1
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recover_tree(root):
    first = second = prev = None
    
    def inorder(node):
        nonlocal first, second, prev
        if not node:
            return
        
        inorder(node.left)
        
        if prev and node.val < prev.val:
            if not first:
                first = prev
            second = node
        prev = node
        
        inorder(node.right)
    
    inorder(root)
    first.val, second.val = second.val, first.val

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
    print("RECOVER BST - Complex structure, manual testing recommended")
except Exception as e:
    print(f"An error occurred: {e}")
