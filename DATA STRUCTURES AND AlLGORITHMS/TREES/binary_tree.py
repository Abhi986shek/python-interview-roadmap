"""
Binary Tree

A tree where each node has at most two children — left and right.
This implementation inserts nodes level by level (like a complete binary tree).

Operations:
    insert   : O(n)  - level order insertion
    display  : O(n)  - level order display

Space Complexity: O(n)
"""

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        # level order insertion — fill left to right
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if not node.left:
                node.left = new_node
                return
            queue.append(node.left)
            if not node.right:
                node.right = new_node
                return
            queue.append(node.right)

    def display_level_order(self):
        if not self.root:
            print("TREE IS EMPTY")
            return
        queue = deque([self.root])
        print("LEVEL ORDER:")
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(str(node.data))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print("  " + " ".join(level))


def main():
    bt = BinaryTree()

    while True:
        print("\n1. INSERT")
        print("2. DISPLAY (LEVEL ORDER)")
        print("3. EXIT")

        try:
            choice = int(input("ENTER YOUR CHOICE: "))

            if choice == 1:
                val = int(input("ENTER VALUE: "))
                bt.insert(val)
                print(f"{val} INSERTED")

            elif choice == 2:
                bt.display_level_order()

            elif choice == 3:
                break

            else:
                print("INVALID CHOICE")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
