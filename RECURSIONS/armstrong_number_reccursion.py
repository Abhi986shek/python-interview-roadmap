"""
Armstrong Number (Recursion & Optimized)

An Armstrong number is a number where the sum of its digits
raised to the power of number of digits equals the number itself.

Example:
153 → 1^3 + 5^3 + 3^3 = 153

Features:
1. RANGE BASED
2. SINGLE CHECK
3. HIGHEST IN RANGE
4. SECOND HIGHEST IN RANGE
"""

# -------- Recursive Approach --------

def number_of_digits(dig_num, n):
    if n == 0:
        return dig_num
    dig_num += 1
    return number_of_digits(dig_num, n // 10)

def is_armstrong(n, sum_val, m, digits):
    if n == 0:
        return m == sum_val
    sum_val += (n % 10) ** digits
    return is_armstrong(n // 10, sum_val, m, digits)

def range_based_recursive(l, u):
    if l > u:
        return
    digits = number_of_digits(0, l)
    if is_armstrong(l, 0, l, digits):
        print(l)
    range_based_recursive(l + 1, u)

def highest_in_range_recursive(l, u):
    if u < l:
        return
    digits = number_of_digits(0, u)
    if is_armstrong(u, 0, u, digits):
        print("HIGHEST ARMSTRONG NUMBER:", u)
        return
    highest_in_range_recursive(l, u - 1)

def second_highest_helper_recursive(l, u, count):
    if u < l:
        return
    digits = number_of_digits(0, u)
    if is_armstrong(u, 0, u, digits):
        count += 1
        if count == 2:
            print("SECOND HIGHEST ARMSTRONG NUMBER:", u)
            return
    second_highest_helper_recursive(l, u - 1, count)

def second_highest_in_range_recursive(l, u):
    second_highest_helper_recursive(l, u, 0)

def single_check_recursive():
    try:
        n = int(input("ENTER THE NUMBER: "))
        digits = number_of_digits(0, n)
        if is_armstrong(n, 0, n, digits):
            print("ENTERED NUMBER IS AN ARMSTRONG NUMBER")
        else:
            print("ENTERED NUMBER IS NOT AN ARMSTRONG NUMBER")
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

def is_armstrong_opt(n: int) -> bool:
    digits = len(str(n))
    return sum(int(d) ** digits for d in str(n)) == n

def range_based_opt(l, u):
    for i in range(l, u + 1):
        if is_armstrong_opt(i):
            print(i)

def highest_in_range_opt(l, u):
    for i in range(u, l - 1, -1):
        if is_armstrong_opt(i):
            print("HIGHEST ARMSTRONG NUMBER:", i)
            return

def second_highest_in_range_opt(l, u):
    count = 0
    for i in range(u, l - 1, -1):
        if is_armstrong_opt(i):
            count += 1
            if count == 2:
                print("SECOND HIGHEST ARMSTRONG NUMBER:", i)
                return

def single_check_opt():
    try:
        n = int(input("ENTER THE NUMBER: "))
        if is_armstrong_opt(n):
            print("ENTERED NUMBER IS AN ARMSTRONG NUMBER")
        else:
            print("ENTERED NUMBER IS NOT AN ARMSTRONG NUMBER")
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