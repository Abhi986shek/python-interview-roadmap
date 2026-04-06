"""
Strong Number (Recursion & Optimized)

A Strong number is a number where the sum of the factorial of its digits equals the number itself.

Example:
145 → 1! + 4! + 5! = 145

Features:
1. RANGE BASED
2. SINGLE CHECK
3. HIGHEST IN RANGE
4. SECOND HIGHEST IN RANGE
"""

# -------- Recursive Approach --------

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def strong_recursive(n, sum_val, m):
    if n == 0:
        return m == sum_val
    sum_val += fact(n % 10)
    return strong_recursive(n // 10, sum_val, m)

def range_based_recursive(l, u):
    if l > u:
        return
    if strong_recursive(l, 0, l):
        print(l)
    range_based_recursive(l + 1, u)

def highest_in_range_recursive(l, u):
    if u < l:
        return
    if strong_recursive(u, 0, u):
        print("HIGHEST STRONG NUMBER:", u)
        return
    highest_in_range_recursive(l, u - 1)

def second_highest_helper_recursive(l, u, count):
    if u < l:
        return
    if strong_recursive(u, 0, u):
        count += 1
        if count == 2:
            print("SECOND HIGHEST STRONG NUMBER:", u)
            return
    second_highest_helper_recursive(l, u - 1, count)

def second_highest_in_range_recursive(l, u):
    second_highest_helper_recursive(l, u, 0)

def single_check_recursive():
    try:
        n = int(input("ENTER THE NUMBER: "))
        if strong_recursive(n, 0, n):
            print("ENTERED NUMBER IS A STRONG NUMBER")
        else:
            print("ENTERED NUMBER IS NOT A STRONG NUMBER")
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

        if choice in [1, 3, 4]:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))

        if choice == 1:
            range_based_recursive(l, u)
        elif choice == 2:
            single_check_recursive()
        elif choice == 3:
            highest_in_range_recursive(l, u)
        elif choice == 4:
            second_highest_in_range_recursive(l, u)
        else:
            print("INVALID CHOICE")

    except ValueError:
        print("INVALID INPUT! PLEASE ENTER NUMBERS ONLY")


if __name__ == "__main__":
    main()


# -------- Optimized Approach --------

def strong_opt(n: int) -> bool:
    return n == sum(fact(int(d)) for d in str(n))

def range_based_opt(l, u):
    for i in range(l, u + 1):
        if strong_opt(i):
            print(i)

def highest_in_range_opt(l, u):
    for i in range(u, l - 1, -1):
        if strong_opt(i):
            print("HIGHEST STRONG NUMBER:", i)
            return

def second_highest_in_range_opt(l, u):
    count = 0
    for i in range(u, l - 1, -1):
        if strong_opt(i):
            count += 1
            if count == 2:
                print("SECOND HIGHEST STRONG NUMBER:", i)
                return

def single_check_opt():
    try:
        n = int(input("ENTER THE NUMBER: "))
        if strong_opt(n):
            print("ENTERED NUMBER IS A STRONG NUMBER")
        else:
            print("ENTERED NUMBER IS NOT A STRONG NUMBER")
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

        if choice in [1, 3, 4]:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))

        if choice == 1:
            range_based_opt(l, u)
        elif choice == 2:
            single_check_opt()
        elif choice == 3:
            highest_in_range_opt(l, u)
        elif choice == 4:
            second_highest_in_range_opt(l, u)
        else:
            print("INVALID CHOICE")

    except ValueError:
        print("INVALID INPUT! PLEASE ENTER NUMBERS ONLY")


if __name__ == "__main__":
    main()