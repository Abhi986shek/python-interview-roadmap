"""
Duck Number (Recursion)

A Duck Number is a number that contains at least one zero,
excluding leading zeros.

Example:
102, 1005

Approach:
- Uses recursion to check each digit
- Returns True if any digit (except leading) is zero
"""

# -------- Basic Approach (Recursion) --------

def is_duck(n):
    if n < 10:
        return False
    if n % 10 == 0:
        return True
    return is_duck(n // 10)

def range_based(l, u):
    if l > u:
        return
    if is_duck(l):
        print(l)
    range_based(l + 1, u)

def highest_in_range(l, u):
    if u < l:
        return
    if is_duck(u):
        print("HIGHEST DUCK NUMBER:", u)
        return
    highest_in_range(l, u - 1)

def second_highest_helper(l, u, count):
    if u < l:
        return
    if is_duck(u):
        count += 1
        if count == 2:
            print("SECOND HIGHEST DUCK NUMBER:", u)
            return
    second_highest_helper(l, u - 1, count)

def second_highest_in_range(l, u):
    second_highest_helper(l, u, 0)

def single_check():
    try:
        n = int(input("ENTER THE NUMBER: "))
        if is_duck(n):
            print("ENTERED NUMBER IS A DUCK NUMBER")
        else:
            print("ENTERED NUMBER IS NOT A DUCK NUMBER")
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
# - Uses string conversion for faster checking
# - Cleaner and more Pythonic

def is_duck_opt(n: int) -> bool:
    return '0' in str(n)[1:]

def range_based(l, u):
    for i in range(l, u + 1):
        if is_duck_opt(i):
            print(i)

def highest_in_range(l, u):
    for i in range(u, l - 1, -1):
        if is_duck_opt(i):
            print("HIGHEST DUCK NUMBER:", i)
            return

def second_highest_in_range(l, u):
    count = 0
    for i in range(u, l - 1, -1):
        if is_duck_opt(i):
            count += 1
            if count == 2:
                print("SECOND HIGHEST DUCK NUMBER:", i)
                return

def single_check(n):
    if is_duck_opt(n):
        print("ENTERED NUMBER IS A DUCK NUMBER")
    else:
        print("ENTERED NUMBER IS NOT A DUCK NUMBER")

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