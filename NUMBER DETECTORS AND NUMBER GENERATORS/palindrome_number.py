"""
Palindrome Number

A number that reads the same forward and backward.

Example:
121, 1331
"""

# -------- Basic Approach --------

def range_based():
    try:
        l = int(input("ENTER THE LOWER LIMIT: "))
        u = int(input("ENTER THE UPPER LIMIT: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    for num in range(l, u + 1):
        n = num
        rev = 0

        while n > 0:
            rev = (rev * 10) + (n % 10)
            n //= 10

        if rev == num:
            print(num)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    original = n
    rev = 0

    while n > 0:
        rev = (rev * 10) + (n % 10)
        n //= 10

    print("THE REVERSED NUMBER IS ->", rev)

    if original == rev:
        print("ENTERED NUMBER IS A PALINDROME")
    else:
        print("ENTERED NUMBER IS NOT A PALINDROME")


def main():
    print("SELECT USE CASE:")
    print("1. RANGE BASED")
    print("2. SINGLE NUMBER CHECK")

    try:
        choice = int(input("ENTER YOUR CHOICE: "))
    except ValueError:
        print("INVALID CHOICE")
        return

    if choice == 1:
        range_based()
    elif choice == 2:
        single_check()
    else:
        print("INVALID CHOICE")


if __name__ == "__main__":
    main()


# -------- Optimized Approach --------
# Improvements:
# - Uses string slicing
# - No manual reversal loop
# - Cleaner and faster

def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]


def range_based(l, u):
    for i in range(l, u + 1):
        if is_palindrome(i):
            print(i)


def single_check(n):
    reversed_num = int(str(n)[::-1])
    print("THE REVERSED NUMBER IS ->", reversed_num)

    if is_palindrome(n):
        print("ENTERED NUMBER IS A PALINDROME")
    else:
        print("ENTERED NUMBER IS NOT A PALINDROME")


def main():
    print("SELECT USE CASE:")
    print("1. RANGE BASED")
    print("2. SINGLE NUMBER CHECK")

    try:
        choice = int(input("ENTER YOUR CHOICE: "))
    except ValueError:
        print("INVALID CHOICE")
        return

    if choice == 1:
        try:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
        except ValueError:
            print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
            return
        range_based(l, u)
    elif choice == 2:
        try:
            n = int(input("ENTER NUMBER: "))
        except ValueError:
            print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
            return
        single_check(n)
    else:
        print("INVALID CHOICE")


if __name__ == "__main__":
    main()