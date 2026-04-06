"""
Stack Using Linked List

A stack implemented using a linked list.
The head of the list acts as the top of the stack.

Operations:
    push   : O(1)
    pop    : O(1)
    peek   : O(1)
    isEmpty: O(1)

Space Complexity: O(n)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        val = self.top.data
        self.top = self.top.next
        self._size -= 1
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def display(self):
        if self.is_empty():
            print("STACK IS EMPTY")
            return
        curr = self.top
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print("STACK (top -> bottom):", " -> ".join(elements))


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
