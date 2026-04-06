"""
Prime Number (Recursion)

A number greater than 1 that has exactly two divisors: 1 and itself.

Example:
2, 3, 5, 7

Approach:
- Uses recursion to check divisibility from n/2 down to 1
- If any divisor is found, number is not prime
"""


# -------- Basic Approach (Recursion) --------

def is_prime(n, i):
    if n <= 1:
        return False
    if i == 1:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i - 1)


def range_based(l, u):
    if l > u:
        return

    if is_prime(l, l // 2):
        print(l)

    range_based(l + 1, u)


def highest_in_range(l, u):
    if u < l:
        return

    if is_prime(u, u // 2):
        print("HIGHEST PRIME NUMBER:", u)
        return

    highest_in_range(l, u - 1)


def second_highest_helper(l, u, count):
    if u < l:
        return

    if is_prime(u, u // 2):
        count += 1
        if count == 2:
            print("SECOND HIGHEST PRIME NUMBER:", u)
            return

    second_highest_helper(l, u - 1, count)


def second_highest_in_range(l, u):
    second_highest_helper(l, u, 0)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER: "))

        if is_prime(n, n // 2):
            print("THE NUMBER IS PRIME")
        else:
            print("THE NUMBER IS NOT PRIME")

    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID NUMBER")


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
# - Reduces checks from n/2 → sqrt(n)
# - Iterative approach is faster and practical

def is_prime_optimized(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2

    return True


def range_based(l, u):
    for i in range(l, u + 1):
        if is_prime_optimized(i):
            print(i)


def highest_in_range(l, u):
    for i in range(u, l - 1, -1):
        if is_prime_optimized(i):
            print("HIGHEST PRIME NUMBER:", i)
            return


def second_highest_in_range(l, u):
    count = 0
    for i in range(u, l - 1, -1):
        if is_prime_optimized(i):
            count += 1
            if count == 2:
                print("SECOND HIGHEST PRIME NUMBER:", i)
                return


def single_check(n):
    if is_prime_optimized(n):
        print("THE NUMBER IS PRIME")
    else:
        print("THE NUMBER IS NOT PRIME")


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