"""
Finds the length of the longest substring without repeating characters.
"""
def length_of_longest_substring(s):

    longest = 0
    current = ""

    for char in s:

        if char in current:
            current = current[current.index(char) + 1:]

        current = current + char

        if len(current) > longest:
            longest = len(current)

    return longest


s = input("Enter a string: ")

if not s.strip():
    print("Input cannot be empty.")
else:
    print("Longest substring length:", length_of_longest_substring(s))
