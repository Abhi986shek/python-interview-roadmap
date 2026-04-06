"""
Finds and prints the first character in the string that does not repeat.
Terminates after finding the first unique instance.
"""
from collections import Counter

try:
    user_input = input("ENTER THE STRING\n")
    counts = Counter(user_input)
    
    for char in user_input:
        if counts[char] == 1:
            print(f"{char} count is = 1")
            break
    else:
        print("No unique character found.")
except Exception as e:
    print(f"An error occurred: {e}")
