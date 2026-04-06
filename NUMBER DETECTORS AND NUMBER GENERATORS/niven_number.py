"""
Niven Number (Harshad Number)

A number that is divisible by the sum of its digits.

Example:
18 → 1 + 8 = 9 → 18 % 9 = 0
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
        digit_sum = 0

        while n > 0:
            digit_sum += n % 10
            n //= 10

        if digit_sum != 0 and num % digit_sum == 0:
            print(num)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    digit_sum = 0
    temp = n

    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    print("SUM OF DIGITS =", digit_sum)

    if digit_sum != 0 and n % digit_sum == 0:
        print("THIS IS A NIVEN NUMBER")
    else:
        print("THIS IS NOT A NIVEN NUMBER")


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
# - Uses string conversion
# - Cleaner and more Pythonic

def is_niven_number(num: int) -> bool:
    digit_sum = sum(int(d) for d in str(num))
    return digit_sum != 0 and num % digit_sum == 0


def range_based(l, u):
    for i in range(l, u + 1):
        if is_niven_number(i):
            print(i)


def single_check(n):
    digit_sum = sum(int(d) for d in str(n))

    print("SUM OF DIGITS =", digit_sum)

    if is_niven_number(n):
        print("THIS IS A NIVEN NUMBER")
    else:
        print("THIS IS NOT A NIVEN NUMBER")


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