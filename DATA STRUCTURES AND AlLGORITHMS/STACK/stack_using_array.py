"""
Stack Using Array

A stack follows LIFO (Last In First Out) order.
Implemented using a Python list as the underlying array.

Operations:
    push   : O(1)
    pop    : O(1)
    peek   : O(1)
    isEmpty: O(1)

Space Complexity: O(n)
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        if self.is_empty():
            print("STACK IS EMPTY")
        else:
            print("STACK (top -> bottom):", self.stack[::-1])


def main():
    s = Stack()

    while True:
        print("\n1. PUSH")
        print("2. POP")
        print("3. PEEK")
        print("4. SIZE")
        print("5. DISPLAY")
        print("6. EXIT")

        try:
            choice = int(input("ENTER YOUR CHOICE: "))

            if choice == 1:
                val = int(input("ENTER VALUE TO PUSH: "))
                s.push(val)
                print(f"{val} PUSHED TO STACK")

            elif choice == 2:
                print(f"POPPED: {s.pop()}")

            elif choice == 3:
                print(f"TOP ELEMENT: {s.peek()}")

            elif choice == 4:
                print(f"STACK SIZE: {s.size()}")

            elif choice == 5:
                s.display()

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
