"""
Prime Number

A number greater than 1 that has exactly two divisors: 1 and itself.

Example:
2, 3, 5, 7
"""

# -------- Basic Approach --------

def prime_in_range():
    try:
        l = int(input("ENTER THE LOWER LIMIT: "))
        u = int(input("ENTER THE UPPER LIMIT: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    for i in range(l, u + 1):
        if i <= 1:
            continue

        flag = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                flag = False
                break

        if flag:
            print(i)


def alternate_primes():
    try:
        l = int(input("ENTER THE LOWER LIMIT: "))
        u = int(input("ENTER THE UPPER LIMIT: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    count = 0

    for i in range(l, u + 1):
        if i <= 1:
            continue

        flag = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                flag = False
                break

        if flag:
            count += 1
            if count % 2 != 0:
                print(i)


def largest_prime():
    try:
        l = int(input("ENTER THE LOWER LIMIT: "))
        u = int(input("ENTER THE UPPER LIMIT: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    for i in range(u, l - 1, -1):
        if i <= 1:
            continue

        flag = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                flag = False
                break

        if flag:
            print(i)
            break


def single_check():
    try:
        n = int(input("ENTER THE NUMBER THAT YOU WANT TO CHECK: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    if n <= 1:
        print(f"{n} IS NOT A PRIME NUMBER :(")
        return

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            print(f"{n} IS NOT A PRIME NUMBER :(")
            return

    print(f"{n} IS A PRIME NUMBER :)")


def main():
    print("SELECT USE CASE:")
    print("1. PRIME NUMBERS IN RANGE")
    print("2. ALTERNATE PRIME NUMBERS")
    print("3. LARGEST PRIME IN RANGE")
    print("4. SINGLE NUMBER CHECK")

    try:
        choice = int(input("ENTER YOUR CHOICE: "))
    except ValueError:
        print("INVALID CHOICE")
        return

    if choice == 1:
        prime_in_range()
    elif choice == 2:
        alternate_primes()
    elif choice == 3:
        largest_prime()
    elif choice == 4:
        single_check()
    else:
        print("INVALID CHOICE")


if __name__ == "__main__":
    main()


# -------- Optimized Approach --------
# Improvements:
# - Prime check reduced to O(√n)
# - Reusable prime function
# - Cleaner structure

import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def prime_in_range(l, u):
    for i in range(l, u + 1):
        if is_prime(i):
            print(i)


def alternate_primes(l, u):
    count = 0
    for i in range(l, u + 1):
        if is_prime(i):
            count += 1
            if count % 2 != 0:
                print(i)


def largest_prime(l, u):
    for i in range(u, l - 1, -1):
        if is_prime(i):
            print(i)
            break


def single_check(n):
    if is_prime(n):
        print(f"{n} IS A PRIME NUMBER :)")
    else:
        print(f"{n} IS NOT A PRIME NUMBER :(")


def main():
    print("SELECT USE CASE:")
    print("1. PRIME NUMBERS IN RANGE")
    print("2. ALTERNATE PRIME NUMBERS")
    print("3. LARGEST PRIME IN RANGE")
    print("4. SINGLE NUMBER CHECK")

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
        prime_in_range(l, u)
    elif choice == 2:
        try:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
        except ValueError:
            print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
            return
        alternate_primes(l, u)
    elif choice == 3:
        try:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
        except ValueError:
            print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
            return
        largest_prime(l, u)
    elif choice == 4:
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