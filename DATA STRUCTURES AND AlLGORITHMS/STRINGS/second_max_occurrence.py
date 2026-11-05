"""
Identifies both the most frequent and the second most frequent characters in a string.
"""
from collections import Counter

user_input = input("ENTER THE STRING\n")

counts = Counter(user_input)

sorted_chars = sorted(
    counts.items(),
    key=lambda x: x[1],
    reverse=True
)

if len(sorted_chars) >= 2:
    char, count = sorted_chars[1]

    print(f"Second highest character: {char}")
    print(f"Count: {count}")
else:
    print("Not enough unique characters.")
