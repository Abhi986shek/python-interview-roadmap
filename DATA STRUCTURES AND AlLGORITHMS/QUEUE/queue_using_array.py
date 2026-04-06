"""
Queue Using Array

A queue follows FIFO (First In First Out) order.
Implemented using a Python list as the underlying array.

Operations:
    enqueue  : O(1)
    dequeue  : O(n) - due to shifting (use collections.deque for O(1))
    peek     : O(1)
    isEmpty  : O(1)

Space Complexity: O(n)
"""


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        if self.is_empty():
            print("QUEUE IS EMPTY")
        else:
            print("QUEUE (front -> rear):", self.queue)


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
