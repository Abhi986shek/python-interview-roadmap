"""
Circular Queue

A fixed-size queue where the rear wraps around to the front when it reaches the end.
Avoids the wasted space problem of a simple array-based queue.

Operations:
    enqueue  : O(1)
    dequeue  : O(1)
    peek     : O(1)
    isEmpty  : O(1)
    isFull   : O(1)

Space Complexity: O(n)
"""


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self.capacity

    def enqueue(self, data):
        if self.is_full():
            raise OverflowError("Queue is full.")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        if self.front == -1:
            self.front = 0
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        val = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self._size -= 1
        if self._size == 0:
            self.front = self.rear = -1
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("QUEUE IS EMPTY")
            return
        print("QUEUE:", self.queue)
        print(f"FRONT INDEX: {self.front}, REAR INDEX: {self.rear}")


def main():
    try:
        cap = int(input("ENTER QUEUE CAPACITY\n"))
        if cap <= 0:
            raise ValueError("Capacity must be greater than 0.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    q = CircularQueue(cap)

    while True:
        print("\n1. ENQUEUE")
        print("2. DEQUEUE")
        print("3. PEEK")
        print("4. DISPLAY")
        print("5. EXIT")

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
                q.display()

            elif choice == 5:
                break

            else:
                print("INVALID CHOICE")

        except (ValueError, IndexError, OverflowError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
