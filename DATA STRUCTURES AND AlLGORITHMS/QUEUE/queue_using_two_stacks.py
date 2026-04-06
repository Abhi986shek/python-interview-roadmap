"""
Queue Using Two Stacks

Simulate a queue using two stacks.
Stack 1 handles enqueue, Stack 2 handles dequeue.
When Stack 2 is empty, pour all elements from Stack 1 into Stack 2.

Operations:
    enqueue  : O(1)
    dequeue  : O(1) amortized

Space Complexity: O(n)
"""


class QueueUsingTwoStacks:
    def __init__(self):
        self.s1 = []  # for enqueue
        self.s2 = []  # for dequeue

    def enqueue(self, data):
        self.s1.append(data)

    def dequeue(self):
        if not self.s1 and not self.s2:
            raise IndexError("Queue is empty.")
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if not self.s1 and not self.s2:
            raise IndexError("Queue is empty.")
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def is_empty(self):
        return not self.s1 and not self.s2


def main():
    q = QueueUsingTwoStacks()

    while True:
        print("\n1. ENQUEUE")
        print("2. DEQUEUE")
        print("3. PEEK")
        print("4. EXIT")

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
                break

            else:
                print("INVALID CHOICE")

        except (ValueError, IndexError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
