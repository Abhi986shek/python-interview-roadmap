"""
Prints the second lowest occurring character in a string.
"""
from collections import Counter

try:
    user_input = input("ENTER THE STRING\n")
    counts = Counter(user_input)
    # Sort characters by frequency (ascending)
    sorted_chars = sorted(counts.items(), key=lambda x: x[1])
    
    if len(sorted_chars) >= 2:
        char, count = sorted_chars[1]
        print(f"{char} IS THE SECOND LOWEST ONE OCCURING WITH A COUNT OF ={count}")
    else:
        print("Not enough unique characters for a second lowest.")
except Exception as e:
    print(f"Error: {e}")