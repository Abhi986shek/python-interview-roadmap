"""
Perfect Number (Recursion & Optimized)

A Perfect number is a number that is equal to the sum of its proper divisors.

Example:
6 → 1 + 2 + 3 = 6

Features:
1. RANGE BASED
2. SINGLE CHECK
3. HIGHEST IN RANGE
4. SECOND HIGHEST IN RANGE
"""

# -------- Recursive Approach --------

def perfect_recursive(n, sum_val, i, m):
    if i == 0:
        return sum_val == m
    if n % i == 0:
        sum_val += i
    return perfect_recursive(n, sum_val, i - 1, m)

def range_based_recursive(l, u):
    if l > u:
        return
    if perfect_recursive(l, 0, l // 2, l):
        print(l)
    range_based_recursive(l + 1, u)

def highest_in_range_recursive(l, u):
    if u < l:
        return
    if perfect_recursive(u, 0, u // 2, u):
        print("HIGHEST PERFECT NUMBER:", u)
        return
    highest_in_range_recursive(l, u - 1)

def second_highest_helper_recursive(l, u, count):
    if u < l:
        return
    if perfect_recursive(u, 0, u // 2, u):
        count += 1
        if count == 2:
            print("SECOND HIGHEST PERFECT NUMBER:", u)
            return
    second_highest_helper_recursive(l, u - 1, count)

def second_highest_in_range_recursive(l, u):
    second_highest_helper_recursive(l, u, 0)

def single_check_recursive():
    try:
        n = int(input("ENTER THE NUMBER: "))
        if perfect_recursive(n, 0, n // 2, n):
            print("ENTERED NUMBER IS A PERFECT NUMBER")
        else:
            print("ENTERED NUMBER IS NOT A PERFECT NUMBER")
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

def perfect_opt(n: int) -> bool:
    return n == sum(i for i in range(1, n // 2 + 1) if n % i == 0)

def range_based_opt(l, u):
    for i in range(l, u + 1):
        if perfect_opt(i):
            print(i)

def highest_in_range_opt(l, u):
    for i in range(u, l - 1, -1):
        if perfect_opt(i):
            print("HIGHEST PERFECT NUMBER:", i)
            return

def second_highest_in_range_opt(l, u):
    count = 0
    for i in range(u, l - 1, -1):
        if perfect_opt(i):
            count += 1
            if count == 2:
                print("SECOND HIGHEST PERFECT NUMBER:", i)
                return

def single_check_opt():
    try:
        n = int(input("ENTER THE NUMBER: "))
        if perfect_opt(n):
            print("ENTERED NUMBER IS A PERFECT NUMBER")
        else:
            print("ENTERED NUMBER IS NOT A PERFECT NUMBER")
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
