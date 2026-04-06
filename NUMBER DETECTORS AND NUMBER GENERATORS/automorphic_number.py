"""
Automorphic Number

A number whose square ends with the same digits as the number itself.

Example:
25 → 25² = 625
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
        m = i * i
        flag = True

        while n > 0:
            if n % 10 != m % 10:
                flag = False
                break
            n //= 10
            m //= 10

        if flag:
            print(i)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER THAT YOU WANT TO CHECK: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    m = n
    sq = n * n
    flag = True

    while n > 0:
        if n % 10 != sq % 10:
            flag = False
            break
        n //= 10
        sq //= 10

    if flag:
        print(f"{m} IS AN AUTOMORPHIC NUMBER")
    else:
        print(f"{m} IS NOT AN AUTOMORPHIC NUMBER")


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
# - Uses string comparison
# - Cleaner and less error-prone

def is_automorphic(num: int) -> bool:
    return str(num * num).endswith(str(num))


def range_based(l, u):
    for i in range(l, u + 1):
        if is_automorphic(i):
            print(i)


def single_check(n):
    if is_automorphic(n):
        print(f"{n} IS AN AUTOMORPHIC NUMBER")
    else:
        print(f"{n} IS NOT AN AUTOMORPHIC NUMBER")


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