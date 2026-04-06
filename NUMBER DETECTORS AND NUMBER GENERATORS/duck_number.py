"""
Duck Number

A number that contains at least one zero, excluding leading zeros.

Example:
102, 1005
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
        has_zero = False

        while n > 0:
            digit = n % 10

            if digit == 0:
                has_zero = True

            n //= 10

        # Exclude numbers starting with 0 → handled implicitly since integers don't store leading zeros
        if has_zero and num >= 10:
            print(num)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    temp = n
    has_zero = False

    while temp > 0:
        digit = temp % 10

        if digit == 0:
            has_zero = True

        temp //= 10

    if has_zero and n >= 10:
        print("THIS IS A DUCK NUMBER")
    else:
        print("THIS IS NOT A DUCK NUMBER")


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
# - Ensures no leading zero
# - Cleaner and O(d)

def is_duck_number(num: int) -> bool:
    num_str = str(num)
    return '0' in num_str[1:]


def range_based(l, u):
    for i in range(l, u + 1):
        if is_duck_number(i):
            print(i)


def single_check(n):
    if is_duck_number(n):
        print("THIS IS A DUCK NUMBER")
    else:
        print("THIS IS NOT A DUCK NUMBER")


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