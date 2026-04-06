"""
HashMap Implementation from Scratch

A hash map stores key-value pairs. Uses an array of buckets with chaining
(linked list at each bucket) to handle collisions.

Operations:
    put    : O(1) average, O(n) worst case (all keys collide)
    get    : O(1) average
    delete : O(1) average

Space Complexity: O(n)
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.buckets = [None] * self.capacity
        self.size = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        idx = self._hash(key)
        node = self.buckets[idx]

        while node:
            if node.key == key:
                node.value = value  # update existing key
                return
            node = node.next

        # insert at head of chain
        new_node = Node(key, value)
        new_node.next = self.buckets[idx]
        self.buckets[idx] = new_node
        self.size += 1

    def get(self, key):
        idx = self._hash(key)
        node = self.buckets[idx]

        while node:
            if node.key == key:
                return node.value
            node = node.next

        raise KeyError(f"Key '{key}' not found.")

    def delete(self, key):
        idx = self._hash(key)
        node = self.buckets[idx]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.buckets[idx] = node.next
                self.size -= 1
                return
            prev = node
            node = node.next

        raise KeyError(f"Key '{key}' not found.")

    def display(self):
        print("HASHMAP CONTENTS:")
        for i, bucket in enumerate(self.buckets):
            if bucket:
                node = bucket
                while node:
                    print(f"  [{i}] {node.key} -> {node.value}")
                    node = node.next


def main():
    hm = HashMap()

    while True:
        print("\n1. PUT (key, value)")
        print("2. GET (key)")
        print("3. DELETE (key)")
        print("4. DISPLAY")
        print("5. EXIT")

        try:
            choice = int(input("ENTER YOUR CHOICE: "))

            if choice == 1:
                key = input("ENTER KEY: ")
                value = input("ENTER VALUE: ")
                hm.put(key, value)
                print(f"STORED: {key} -> {value}")

            elif choice == 2:
                key = input("ENTER KEY: ")
                print(f"VALUE: {hm.get(key)}")

            elif choice == 3:
                key = input("ENTER KEY: ")
                hm.delete(key)
                print(f"DELETED KEY: {key}")

            elif choice == 4:
                hm.display()

            elif choice == 5:
                break

            else:
                print("INVALID CHOICE")

        except (KeyError, ValueError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
