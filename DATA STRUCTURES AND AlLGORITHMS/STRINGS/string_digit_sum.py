"""
Extracts all numerical sequences from a string and calculates their total sum.
Example: 'abc10def20' returns 30.
"""
import re

try:
    user_input = input("ENTER THE STRING\n")
    # Finds all sequences of digits (e.g., '123' stays 123, not 1, 2, 3)
    numbers = re.findall(r'\d+', user_input)
    total_sum = sum(int(num) for num in numbers)
    
    print(f"THE SUM OF ALL THE NUMBERS IS = {total_sum}")
except Exception as e:
    print(f"An error occurred: {e}")
