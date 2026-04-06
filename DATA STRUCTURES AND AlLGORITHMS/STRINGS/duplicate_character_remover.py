"""
Removes all duplicate characters from a string, keeping only the first occurrence.
Optimized using a set for O(N) time complexity.
"""
try:
    user_input = input("ENTER THE STRING\n")
    seen = set()
    result = []

    for char in user_input:
        if char not in seen:
            result.append(char)
            seen.add(char)

    print("AFTER REMOVING THE DUPLICATE LETTERS")
    print("".join(result))
except Exception as e:
    print(f"An error occurred: {e}")
