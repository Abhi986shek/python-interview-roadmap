"""
Sorts the characters of a string in ascending alphabetical order.
"""
try:
    user_input = input("ENTER THE STRING\n")
    # Python's sorted() is highly optimized (Timsort)
    sorted_chars = sorted(user_input)

    print("AFTER ASCENDING THE STRING")
    print("".join(sorted_chars))
except Exception as e:
    print(f"An error occurred: {e}")
