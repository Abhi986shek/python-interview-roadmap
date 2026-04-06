"""
Deque (Double Ended Queue)

Elements can be inserted and removed from both the front and the rear.
Implemented using a doubly linked list for O(1) operations on both ends.

Operations:
    add_front    : O(1)
    add_rear     : O(1)
    remove_front : O(1)
    remove_rear  : O(1)
    peek_front   : O(1)
    peek_rear    : O(1)

Space Complexity: O(n)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self.front is None

    def add_front(self, data):
        node = Node(data)
        if self.is_empty():
            self.front = self.rear = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self._size += 1

    def add_rear(self, data):
        node = Node(data)
        if self.is_empty():
            self.front = self.rear = node
        else:
            node.prev = self.rear
            self.rear.next = node
            self.rear = node
        self._size += 1

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        val = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        self._size -= 1
        return val

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        val = self.rear.data
        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None
        else:
            self.front = None
        self._size -= 1
        return val

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.front.data

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.rear.data

    def display(self):
        if self.is_empty():
            print("DEQUE IS EMPTY")
            return
        curr = self.front
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print("DEQUE (front -> rear):", " <-> ".join(elements))


def main():
    dq = Deque()

    while True:
        print("\n1. ADD AT FRONT")
        print("2. ADD AT REAR")
        print("3. REMOVE FROM FRONT")
        print("4. REMOVE FROM REAR")
        print("5. PEEK FRONT")
        print("6. PEEK REAR")
        print("7. DISPLAY")
        print("8. EXIT")

        try:
            choice = int(input("ENTER YOUR CHOICE: "))

            if choice == 1:
                val = int(input("ENTER VALUE: "))
                dq.add_front(val)

            elif choice == 2:
                val = int(input("ENTER VALUE: "))
                dq.add_rear(val)

            elif choice == 3:
                print(f"REMOVED FROM FRONT: {dq.remove_front()}")

            elif choice == 4:
                print(f"REMOVED FROM REAR: {dq.remove_rear()}")

            elif choice == 5:
                print(f"FRONT: {dq.peek_front()}")

            elif choice == 6:
                print(f"REAR: {dq.peek_rear()}")

            elif choice == 7:
                dq.display()

            elif choice == 8:
                break

            else:
                print("INVALID CHOICE")

        except (ValueError, IndexError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
