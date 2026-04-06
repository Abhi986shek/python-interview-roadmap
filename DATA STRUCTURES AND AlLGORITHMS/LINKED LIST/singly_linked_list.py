"""
Singly Linked List

A linear data structure where each node holds data and a pointer to the next node.
The last node points to None.

Operations:
    insert_at_beginning  : O(1)
    insert_at_end        : O(n)
    insert_at_position   : O(n)
    delete_by_value      : O(n)
    search               : O(n)
    display              : O(n)

Space Complexity: O(n)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
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

    def insert_at_position(self, data, pos):
        if pos == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        curr = self.head
        for _ in range(pos - 1):
            if not curr:
                raise IndexError("Position out of range.")
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def delete_by_value(self, data):
        if not self.head:
            raise ValueError("List is empty.")
        if self.head.data == data:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                return
            curr = curr.next
        raise ValueError(f"{data} not found in the list.")

    def search(self, data):
        curr = self.head
        idx = 0
        while curr:
            if curr.data == data:
                return idx
            curr = curr.next
            idx += 1
        return -1

    def display(self):
        if not self.head:
            print("LIST IS EMPTY")
            return
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements) + " -> None")


def main():
    ll = SinglyLinkedList()

    while True:
        print("\n1. INSERT AT BEGINNING")
        print("2. INSERT AT END")
        print("3. INSERT AT POSITION")
        print("4. DELETE BY VALUE")
        print("5. SEARCH")
        print("6. DISPLAY")
        print("7. EXIT")

        try:
            choice = int(input("ENTER YOUR CHOICE: "))

            if choice == 1:
                val = int(input("ENTER VALUE: "))
                ll.insert_at_beginning(val)

            elif choice == 2:
                val = int(input("ENTER VALUE: "))
                ll.insert_at_end(val)

            elif choice == 3:
                val = int(input("ENTER VALUE: "))
                pos = int(input("ENTER POSITION: "))
                ll.insert_at_position(val, pos)

            elif choice == 4:
                val = int(input("ENTER VALUE TO DELETE: "))
                ll.delete_by_value(val)

            elif choice == 5:
                val = int(input("ENTER VALUE TO SEARCH: "))
                idx = ll.search(val)
                if idx != -1:
                    print(f"{val} FOUND AT INDEX {idx}")
                else:
                    print(f"{val} NOT FOUND")

            elif choice == 6:
                ll.display()

            elif choice == 7:
                break

            else:
                print("INVALID CHOICE")

        except (ValueError, IndexError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
