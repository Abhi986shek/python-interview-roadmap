"""
Queue Using Linked List

A queue implemented using a linked list.
Front pointer for dequeue, rear pointer for enqueue — both O(1).

Operations:
    enqueue  : O(1)
    dequeue  : O(1)
    peek     : O(1)
    isEmpty  : O(1)

Space Complexity: O(n)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.rear:
            self.rear.next = node
        self.rear = node
        if not self.front:
            self.front = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        val = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self._size -= 1
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.front.data

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size

    def display(self):
        if self.is_empty():
            print("QUEUE IS EMPTY")
            return
        curr = self.front
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print("QUEUE (front -> rear):", " -> ".join(elements))


def main():
    q = Queue()

    while True:
        print("\n1. ENQUEUE")
        print("2. DEQUEUE")
        print("3. PEEK")
        print("4. SIZE")
        print("5. DISPLAY")
        print("6. EXIT")

        try:
            choice = int(input("ENTER YOUR CHOICE: "))

            if choice == 1:
                val = int(input("ENTER VALUE TO ENQUEUE: "))
                q.enqueue(val)
                print(f"{val} ADDED TO QUEUE")

            elif choice == 2:
                print(f"DEQUEUED: {q.dequeue()}")

            elif choice == 3:
                print(f"FRONT ELEMENT: {q.peek()}")

            elif choice == 4:
                print(f"QUEUE SIZE: {q.size()}")

            elif choice == 5:
                q.display()

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
