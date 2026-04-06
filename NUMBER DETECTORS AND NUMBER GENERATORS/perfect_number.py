"""
Perfect Number

A number equal to the sum of its proper divisors (excluding itself).

Example:
6 → 1 + 2 + 3 = 6
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

        for j in range(1, i // 2 + 1):
            if i % j == 0:
                sum_val += j

        if sum_val == i:
            print(i)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER, YOU WANNA CHECK: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    sum_val = 0
    i = 1

    while i < n:
        if n % i == 0:
            sum_val += i
        i += 1

    if n == sum_val:
        print("\nAS THE SUM OF ITS DIVISORS IS EQUAL TO IT...\n")
        print("ENTERED NUMBER IS A PERFECT NUMBER :)")
    else:
        print("\nAS THE SUM OF ITS DIVISORS IS NOT EQUAL TO IT...\n")
        print("ENTERED NUMBER IS NOT A PERFECT NUMBER :(")


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
# - Check divisors only up to sqrt(n)
# - Reduces time complexity from O(n) to O(√n)
# - Reusable function

import math

def is_perfect(num: int) -> bool:
    if num < 2:
        return False

    sum_val = 1
    root = int(math.sqrt(num))

    for i in range(2, root + 1):
        if num % i == 0:
            sum_val += i
            if i != num // i:
                sum_val += num // i

    return sum_val == num


def range_based(l, u):
    for i in range(l, u + 1):
        if is_perfect(i):
            print(i)


def single_check(n):
    if is_perfect(n):
        print("\nAS THE SUM OF ITS DIVISORS IS EQUAL TO IT...\n")
        print("ENTERED NUMBER IS A PERFECT NUMBER :)")
    else:
        print("\nAS THE SUM OF ITS DIVISORS IS NOT EQUAL TO IT...\n")
        print("ENTERED NUMBER IS NOT A PERFECT NUMBER :(")


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