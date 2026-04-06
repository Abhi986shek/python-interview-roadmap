"""
Identifies both the most frequent and the second most frequent characters in a string.
"""
from collections import Counter

try:
    user_input = input("ENTER THE STRING\n")
    counts = Counter(user_input)

    # Sort counts by value descending
    sorted_counts = counts.most_common()

    if len(sorted_counts) < 2:
        print("Not enough unique characters to find a second maximum.")
    else:
        max1_char, max1_val = sorted_counts[0]
        max2_char, max2_val = sorted_counts[1]

        print(f"{max1_char} IS THE HIGHEST ONE OCCURING WITH A COUNT OF ={max1_val}")
        print(f"{max2_char} IS THE SECOND HIGHEST ONE OCCURING WITH A COUNT OF ={max2_val}")
except Exception as e:
    print(f"An error occurred: {e}")
