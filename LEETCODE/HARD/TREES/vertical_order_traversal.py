"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- 0 <= Node.val <= 1000
"""

from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_traversal(root):
    if not root:
        return []
    
    column_table = defaultdict(list)
    queue = deque([(root, 0, 0)])
    
    while queue:
        node, row, col = queue.popleft()
        column_table[col].append((row, node.val))
        
        if node.left:
            queue.append((node.left, row + 1, col - 1))
        if node.right:
            queue.append((node.right, row + 1, col + 1))
    
    result = []
    for col in sorted(column_table.keys()):
        column_table[col].sort()
        result.append([val for row, val in column_table[col]])
    
    return result

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
    print(f"VERTICAL ORDER: {vertical_traversal(root)}")
except Exception as e:
    print(f"An error occurred: {e}")
