"""
Spy Number

A number where the sum of its digits equals the product of its digits.

Example:
1124 → sum = 8, product = 8
"""

# -------- Basic Approach --------

def range_based():
    try:
        l = int(input("ENTER THE LOWER LIMIT: "))
        u = int(input("ENTER THE UPPER LIMIT: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    for i in range(l, u + 1):
        n = i
        m = i
        sum_val = 0
        prod = 1

        while n > 0:
            sum_val += n % 10
            n //= 10

        while m > 0:
            prod *= m % 10
            m //= 10

        if sum_val == prod:
            print(i)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER THAT YOU WANT TO CHECK: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    sum_val = 0
    prod = 1
    m = n

    while n > 0:
        sum_val += n % 10
        prod *= n % 10
        n //= 10

    print("\nTHE SUM OF THE DIGITS IS =", sum_val)
    print("THE PRODUCT OF THE DIGITS IS =", prod)
    print()

    if sum_val == prod:
        print("AS,")
        print("SUM OF THE DIGITS = THE PRODUCT OF THE DIGITS\n")
        print(f"{m} IS A SPY NUMBER")
    else:
        print("AS,")
        print("SUM OF THE DIGITS != THE PRODUCT OF THE DIGITS\n")
        print(f"{m} IS NOT A SPY NUMBER")


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
# - Single pass for sum and product
# - Uses string iteration for cleaner logic
# - Avoids duplicate loops

def is_spy_number(num: int):
    digits = [int(d) for d in str(num)]
    sum_val = sum(digits)

    prod = 1
    for d in digits:
        prod *= d

    return sum_val == prod, sum_val, prod


def range_based(l, u):
    for i in range(l, u + 1):
        result, _, _ = is_spy_number(i)
        if result:
            print(i)


def single_check(n):
    result, sum_val, prod = is_spy_number(n)

    print("\nTHE SUM OF THE DIGITS IS =", sum_val)
    print("THE PRODUCT OF THE DIGITS IS =", prod)
    print()

    if result:
        print("AS,")
        print("SUM OF THE DIGITS = THE PRODUCT OF THE DIGITS\n")
        print(f"{n} IS A SPY NUMBER")
    else:
        print("AS,")
        print("SUM OF THE DIGITS != THE PRODUCT OF THE DIGITS\n")
        print(f"{n} IS NOT A SPY NUMBER")


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