"""
Max Heap

A complete binary tree where every parent node is greater than or equal to its children.
The maximum element is always at the root.
Stored as an array — for node at index i:
    Left child  : 2*i + 1
    Right child : 2*i + 2
    Parent      : (i - 1) // 2

Operations:
    insert      : O(log n)
    extract_max : O(log n)
    peek_max    : O(1)

Space Complexity: O(n)
"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _heapify_up(self, i):
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            p = self._parent(i)
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p

    def _heapify_down(self, i):
        n = len(self.heap)
        largest = i
        l, r = self._left(i), self._right(i)

        if l < n and self.heap[l] > self.heap[largest]:
            largest = l
        if r < n and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            raise IndexError("Heap is empty.")
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def peek_max(self):
        if not self.heap:
            raise IndexError("Heap is empty.")
        return self.heap[0]

    def display(self):
        print(f"HEAP ARRAY: {self.heap}")


def main():
    h = MaxHeap()

    while True:
        print("\n1. INSERT")
        print("2. EXTRACT MAX")
        print("3. PEEK MAX")
        print("4. DISPLAY")
        print("5. EXIT")

        try:
            choice = int(input("ENTER YOUR CHOICE: "))

            if choice == 1:
                val = int(input("ENTER VALUE: "))
                h.insert(val)
                print(f"{val} INSERTED")

            elif choice == 2:
                print(f"EXTRACTED MAX: {h.extract_max()}")

            elif choice == 3:
                print(f"MAX ELEMENT: {h.peek_max()}")

            elif choice == 4:
                h.display()

            elif choice == 5:
                break

            else:
                print("INVALID CHOICE")

        except (ValueError, IndexError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
