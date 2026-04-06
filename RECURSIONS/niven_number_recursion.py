"""
Niven Number / Harshad Number (Recursion)

A Niven (Harshad) Number is a number that is divisible by 
the sum of its digits.

Example:
18 → 1 + 8 = 9 → 18 % 9 = 0

Approach:
- Uses recursion to calculate the sum of digits
- Checks divisibility of the original number by the sum
"""

# -------- Basic Approach (Recursion) --------

def is_niven(n, sum_val=0, original=None):
    if original is None:
        original = n
    if n == 0:
        if sum_val == 0:
            return False
        return original % sum_val == 0
    sum_val += n % 10
    return is_niven(n // 10, sum_val, original)

def range_based(l, u):
    if l > u:
        return
    if is_niven(l):
        print(l)
    range_based(l + 1, u)

def highest_in_range(l, u):
    if u < l:
        return
    if is_niven(u):
        print("HIGHEST NIVEN NUMBER:", u)
        return
    highest_in_range(l, u - 1)

def second_highest_helper(l, u, count):
    if u < l:
        return
    if is_niven(u):
        count += 1
        if count == 2:
            print("SECOND HIGHEST NIVEN NUMBER:", u)
            return
    second_highest_helper(l, u - 1, count)

def second_highest_in_range(l, u):
    second_highest_helper(l, u, 0)

def single_check():
    try:
        n = int(input("ENTER THE NUMBER: "))
        if is_niven(n):
            print("ENTERED NUMBER IS A NIVEN NUMBER")
        else:
            print("ENTERED NUMBER IS NOT A NIVEN NUMBER")
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A NUMBER")


def main():
    try:
        print("SELECT USE CASE:")
        print("1. RANGE BASED")
        print("2. SINGLE CHECK")
        print("3. HIGHEST IN RANGE")
        print("4. SECOND HIGHEST IN RANGE")

        choice = int(input("ENTER YOUR CHOICE: "))

        if choice == 1:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
            range_based(l, u)

        elif choice == 2:
            single_check()

        elif choice == 3:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
            highest_in_range(l, u)

        elif choice == 4:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
            second_highest_in_range(l, u)

        else:
            print("INVALID CHOICE")
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER NUMBERS ONLY")


if __name__ == "__main__":
    main()


# -------- Optimized Approach --------
# Improvements:
# - Uses string conversion for faster sum calculation
# - Cleaner and more Pythonic

def is_niven_opt(n: int) -> bool:
    sum_digits = sum(int(d) for d in str(n))
    return n % sum_digits == 0

def range_based(l, u):
    for i in range(l, u + 1):
        if is_niven_opt(i):
            print(i)

def highest_in_range(l, u):
    for i in range(u, l - 1, -1):
        if is_niven_opt(i):
            print("HIGHEST NIVEN NUMBER:", i)
            return

def second_highest_in_range(l, u):
    count = 0
    for i in range(u, l - 1, -1):
        if is_niven_opt(i):
            count += 1
            if count == 2:
                print("SECOND HIGHEST NIVEN NUMBER:", i)
                return

def single_check(n):
    if is_niven_opt(n):
        print("ENTERED NUMBER IS A NIVEN NUMBER")
    else:
        print("ENTERED NUMBER IS NOT A NIVEN NUMBER")

def main():
    try:
        print("SELECT USE CASE:")
        print("1. RANGE BASED")
        print("2. SINGLE CHECK")
        print("3. HIGHEST IN RANGE")
        print("4. SECOND HIGHEST IN RANGE")

        choice = int(input("ENTER YOUR CHOICE: "))

        if choice == 1:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
            range_based(l, u)

        elif choice == 2:
            n = int(input("ENTER NUMBER: "))
            single_check(n)

        elif choice == 3:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
            highest_in_range(l, u)

        elif choice == 4:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
            second_highest_in_range(l, u)

        else:
            print("INVALID CHOICE")
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER VALID NUMBERS")

if __name__ == "__main__":
    main()