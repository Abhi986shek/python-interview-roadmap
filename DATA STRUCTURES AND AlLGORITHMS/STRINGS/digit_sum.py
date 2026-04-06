"""
Module: digit_sum.py
Description: Calculates the arithmetic sum of all numeric digits found within a string.
Logic: Filters numeric characters using .isdigit(), converts them to integers, 
and calculates the sum.
"""

def sum_digits():
    try:
        s = input("ENTER THE STRING: ")
        total = sum(int(char) for char in s if char.isdigit())
        
        print(f"\nTHE SUM OF NUMBERS IS: {total}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    sum_digits()