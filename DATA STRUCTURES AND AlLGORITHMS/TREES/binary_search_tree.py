"""
Binary Search Tree (BST)

A binary tree where for every node:
    - all values in the left subtree are smaller
    - all values in the right subtree are greater

Operations:
    insert  : O(log n) average, O(n) worst case (skewed tree)
    search  : O(log n) average
    delete  : O(log n) average

Space Complexity: O(n)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if not node:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if not node:
            return False
        if node.data == data:
            return True
        if data < node.data:
            return self._search(node.left, data)
        return self._search(node.right, data)

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if not node:
            raise ValueError(f"{data} not found in tree.")
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            # node with one or no child
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # node with two children — replace with inorder successor
            successor = node.right
            while successor.left:
                successor = successor.left
            node.data = successor.data
            node.right = self._delete(node.right, successor.data)
        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.data)
            self._inorder(node.right, result)


def main():
    bst = BST()

    while True:
        print("\n1. INSERT")
        print("2. SEARCH")
        print("3. DELETE")
        print("4. DISPLAY INORDER")
        print("5. EXIT")

        try:
            choice = int(input("ENTER YOUR CHOICE: "))

            if choice == 1:
                val = int(input("ENTER VALUE: "))
                bst.insert(val)
                print(f"{val} INSERTED")

            elif choice == 2:
                val = int(input("ENTER VALUE TO SEARCH: "))
                if bst.search(val):
                    print(f"{val} FOUND IN THE TREE")
                else:
                    print(f"{val} NOT FOUND")

            elif choice == 3:
                val = int(input("ENTER VALUE TO DELETE: "))
                bst.delete(val)
                print(f"{val} DELETED")

            elif choice == 4:
                print(f"INORDER TRAVERSAL: {bst.inorder()}")

            elif choice == 5:
                break

            else:
                print("INVALID CHOICE")

        except (ValueError, IndexError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
