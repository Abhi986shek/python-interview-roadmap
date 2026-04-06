"""
Tree Traversals

Four ways to visit every node in a binary tree:

    Inorder    (Left, Root, Right)  : gives sorted order for BST
    Preorder   (Root, Left, Right)  : useful for copying a tree
    Postorder  (Left, Right, Root)  : useful for deleting a tree
    Level Order (BFS)               : visits level by level

Time Complexity  : O(n) for all traversals
Space Complexity : O(n) for all traversals
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


def inorder(node, result):
    if node:
        inorder(node.left, result)
        result.append(node.data)
        inorder(node.right, result)


def preorder(node, result):
    if node:
        result.append(node.data)
        preorder(node.left, result)
        preorder(node.right, result)


def postorder(node, result):
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.data)


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


try:
    raw = input("ENTER TREE ELEMENTS (space separated, inserted level by level)\n")
    values = list(map(int, raw.split()))

    if not values:
        raise ValueError("Input cannot be empty.")

    root = None
    for val in values:
        root = insert(root, val)

    res_in, res_pre, res_post = [], [], []
    inorder(root, res_in)
    preorder(root, res_pre)
    postorder(root, res_post)

    print(f"INORDER    : {res_in}")
    print(f"PREORDER   : {res_pre}")
    print(f"POSTORDER  : {res_post}")
    print(f"LEVEL ORDER: {level_order(root)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
