"""
Doubly Linked List

Each node holds data, a pointer to the next node, and a pointer to the previous node.
Allows traversal in both directions.

Operations:
    insert_at_beginning  : O(1)
    insert_at_end        : O(n)
    delete_by_value      : O(n)
    traverse_forward     : O(n)
    traverse_backward    : O(n)

Space Complexity: O(n)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def delete_by_value(self, data):
        if not self.head:
            raise ValueError("List is empty.")
        curr = self.head
        while curr:
            if curr.data == data:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                return
            curr = curr.next
        raise ValueError(f"{data} not found in the list.")

    def traverse_forward(self):
        if not self.head:
            print("LIST IS EMPTY")
            return
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print("FORWARD: " + " <-> ".join(elements) + " -> None")

    def traverse_backward(self):
        if not self.head:
            print("LIST IS EMPTY")
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.prev
        print("BACKWARD: " + " <-> ".join(elements) + " -> None")


def main():
    dll = DoublyLinkedList()

    while True:
        print("\n1. INSERT AT BEGINNING")
        print("2. INSERT AT END")
        print("3. DELETE BY VALUE")
        print("4. TRAVERSE FORWARD")
        print("5. TRAVERSE BACKWARD")
        print("6. EXIT")

        try:
            choice = int(input("ENTER YOUR CHOICE: "))

            if choice == 1:
                val = int(input("ENTER VALUE: "))
                dll.insert_at_beginning(val)

            elif choice == 2:
                val = int(input("ENTER VALUE: "))
                dll.insert_at_end(val)

            elif choice == 3:
                val = int(input("ENTER VALUE TO DELETE: "))
                dll.delete_by_value(val)

            elif choice == 4:
                dll.traverse_forward()

            elif choice == 5:
                dll.traverse_backward()

            elif choice == 6:
                break

            else:
                print("INVALID CHOICE")

        except (ValueError, IndexError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
