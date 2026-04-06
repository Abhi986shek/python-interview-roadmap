"""
Strong Number

A number where the sum of the factorial of its digits equals the number.

Example:
145 → 1! + 4! + 5! = 145
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
        sum_val = 0
        m = i

        while m > 0:
            digit = m % 10
            fact = 1

            for j in range(1, digit + 1):
                fact *= j

            sum_val += fact
            m //= 10

        if sum_val == i:
            print(i)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER THAT YOU WANT TO CHECK: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    m = n
    sum_val = 0

    while n > 0:
        digit = n % 10
        fact = 1

        for i in range(1, digit + 1):
            fact *= i

        sum_val += fact
        n //= 10

    print(f"\nSUM OF FACTORIALS = {sum_val}")

    if m == sum_val:
        print(f"{m} IS A STRONG NUMBER :)")
    else:
        print(f"{m} IS NOT A STRONG NUMBER :(")


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
# - Precompute factorials (0–9)
# - Avoid repeated calculations
# - Faster for large ranges

def precompute_factorials():
    fact = [1] * 10
    for i in range(2, 10):
        fact[i] = fact[i - 1] * i
    return fact


def is_strong_number(num: int, fact) -> bool:
    return sum(fact[int(d)] for d in str(num)) == num


def range_based(l, u):
    fact = precompute_factorials()

    for i in range(l, u + 1):
        if is_strong_number(i, fact):
            print(i)


def single_check(n):
    fact = precompute_factorials()
    sum_val = sum(fact[int(d)] for d in str(n))

    print(f"\nSUM OF FACTORIALS = {sum_val}")

    if is_strong_number(n, fact):
        print(f"{n} IS A STRONG NUMBER :)")
    else:
        print(f"{n} IS NOT A STRONG NUMBER :(")


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