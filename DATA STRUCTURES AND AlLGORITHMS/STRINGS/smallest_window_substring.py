"""
Finds the smallest window in s1 containing all characters of s2.
"""
from collections import Counter

def find_smallest_window(s1, s2):

    smallest = ""

    for i in range(len(s1)):

        current = ""

        for j in range(i, len(s1)):

            current = current + s1[j]

            valid = True

            for char in s2:
                if current.count(char) < s2.count(char):
                    valid = False
                    break

            if valid:
                if smallest == "" or len(current) < len(smallest):
                    smallest = current

                break

    return smallest


try:
    s1 = input("ENTER THE MAIN STRING\n")
    s2 = input("ENTER THE PATTERN STRING\n")
    if not s1.strip() or not s2.strip():
        raise ValueError("Both inputs cannot be empty.")
    result = find_smallest_window(s1, s2)
    print(f"Smallest window: {result if result else 'No window found'}")
except Exception as e:
    print(f"Error: {e}")
