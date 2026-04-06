"""
Circular Linked List

A singly linked list where the last node points back to the head instead of None.
Useful for round-robin scheduling and circular buffers.

Operations:
    insert_at_beginning  : O(n) - need to update last node's next
    insert_at_end        : O(n)
    delete_by_value      : O(n)
    display              : O(n)

Space Complexity: O(n)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        new_node.next = self.head
        self.head = new_node
        curr.next = self.head

    def delete_by_value(self, data):
        if not self.head:
            raise ValueError("List is empty.")

        # only one node
        if self.head.data == data and self.head.next == self.head:
            self.head = None
            return

        # deleting head
        if self.head.data == data:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
            return

        curr = self.head
        while curr.next != self.head:
            if curr.next.data == data:
                curr.next = curr.next.next
                return
            curr = curr.next

        raise ValueError(f"{data} not found in the list.")

    def display(self):
        if not self.head:
            print("LIST IS EMPTY")
            return
        curr = self.head
        elements = []
        while True:
            elements.append(str(curr.data))
            curr = curr.next
            if curr == self.head:
                break
        print(" -> ".join(elements) + " -> (back to head)")


def main():
    cll = CircularLinkedList()

    while True:
        print("\n1. INSERT AT BEGINNING")
        print("2. INSERT AT END")
        print("3. DELETE BY VALUE")
        print("4. DISPLAY")
        print("5. EXIT")

        try:
            choice = int(input("ENTER YOUR CHOICE: "))

            if choice == 1:
                val = int(input("ENTER VALUE: "))
                cll.insert_at_beginning(val)

            elif choice == 2:
                val = int(input("ENTER VALUE: "))
                cll.insert_at_end(val)

            elif choice == 3:
                val = int(input("ENTER VALUE TO DELETE: "))
                cll.delete_by_value(val)

            elif choice == 4:
                cll.display()

            elif choice == 5:
                break

            else:
                print("INVALID CHOICE")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
