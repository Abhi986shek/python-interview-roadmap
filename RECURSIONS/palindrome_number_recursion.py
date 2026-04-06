"""
Palindrome Number (Recursion & Optimized)

A Palindrome number is a number that reads the same backward as forward.

Example:
121 → 121

Features:
1. RANGE BASED
2. SINGLE CHECK
3. HIGHEST IN RANGE
4. SECOND HIGHEST IN RANGE
"""

# -------- Recursive Approach --------

def palindrome_recursive(n, sum_val, m):
    if n == 0:
        return m == sum_val
    sum_val = (n % 10) + sum_val * 10
    return palindrome_recursive(n // 10, sum_val, m)

def range_based_recursive(l, u):
    if l > u:
        return
    if palindrome_recursive(l, 0, l):
        print(l)
    range_based_recursive(l + 1, u)

def highest_in_range_recursive(l, u):
    if u < l:
        return
    if palindrome_recursive(u, 0, u):
        print("HIGHEST PALINDROME NUMBER:", u)
        return
    highest_in_range_recursive(l, u - 1)

def second_highest_helper_recursive(l, u, count):
    if u < l:
        return
    if palindrome_recursive(u, 0, u):
        count += 1
        if count == 2:
            print("SECOND HIGHEST PALINDROME NUMBER:", u)
            return
    second_highest_helper_recursive(l, u - 1, count)

def second_highest_in_range_recursive(l, u):
    second_highest_helper_recursive(l, u, 0)

def single_check_recursive():
    try:
        n = int(input("ENTER THE NUMBER: "))
        if palindrome_recursive(n, 0, n):
            print("ENTERED NUMBER IS A PALINDROME NUMBER")
        else:
            print("ENTERED NUMBER IS NOT A PALINDROME NUMBER")
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

def is_palindrome_opt(n: int) -> bool:
    return str(n) == str(n)[::-1]

def range_based_opt(l, u):
    for i in range(l, u + 1):
        if is_palindrome_opt(i):
            print(i)

def highest_in_range_opt(l, u):
    for i in range(u, l - 1, -1):
        if is_palindrome_opt(i):
            print("HIGHEST PALINDROME NUMBER:", i)
            return

def second_highest_in_range_opt(l, u):
    count = 0
    for i in range(u, l - 1, -1):
        if is_palindrome_opt(i):
            count += 1
            if count == 2:
                print("SECOND HIGHEST PALINDROME NUMBER:", i)
                return

def single_check_opt():
    try:
        n = int(input("ENTER THE NUMBER: "))
        if is_palindrome_opt(n):
            print("ENTERED NUMBER IS A PALINDROME NUMBER")
        else:
            print("ENTERED NUMBER IS NOT A PALINDROME NUMBER")
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