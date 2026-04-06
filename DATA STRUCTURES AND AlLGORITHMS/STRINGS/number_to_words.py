"""
Converts a numeric value into Indian numbering system words (Crores, Lakhs, etc.).
"""
def convert(n, suffix):
    one = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
           "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    two = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    res = ""
    if n <= 19:
        res = one[n]
    else:
        res = two[n // 10] + (" " + one[n % 10] if n % 10 != 0 else "")
    
    if n != 0:
        print(f"{res} {suffix}", end=" ")

try:
    num = int(input("ENTER THE NUMBER\n"))
    if num < 0:
        print("Error: Negative numbers are not supported.")
    elif num == 0:
        print("zero")
    else:
        convert(num // 10000000, "crore")
        convert((num // 100000) % 100, "lakhs")
        convert((num // 1000) % 100, "thousand")
        convert((num // 100) % 10, "hundred")
        convert(num % 100, "")
        print()
except ValueError:
    print("Error: Please enter a valid integer.")