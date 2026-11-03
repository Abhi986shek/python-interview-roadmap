
"""
Diamond Pattern Collection
Using basic nested loops
"""


# 1. Solid Diamond
def solid_diamond(n):
    if n % 2 == 0:
        n += 1

    star = 1
    space = n // 2

    for i in range(1, n + 1):
        for j in range(1, space + 1):
            print(" ", end="")

        for j in range(1, star + 1):
            print("*", end="")

        print()

        if i <= n // 2:
            star += 2
            space -= 1
        else:
            star -= 2
            space += 1


# 2. Hollow Diamond
def hollow_diamond(n):
    if n % 2 == 0:
        n += 1

    star = 1
    space = n // 2

    for i in range(1, n + 1):
        for j in range(1, space + 1):
            print(" ", end="")

        for j in range(1, star + 1):
            if j == 1 or j == star:
                print("*", end="")
            else:
                print(" ", end="")

        print()

        if i <= n // 2:
            star += 2
            space -= 1
        else:
            star -= 2
            space += 1


# 3. Inverted Diamond / Butterfly
def inverted_diamond_butterfly(n):
    if n % 2 == 0:
        n += 1

    star = n // 2
    space = 1

    for i in range(1, n + 1):
        for j in range(1, star + 1):
            print("*", end="")

        for j in range(1, space + 1):
            print(" ", end="")

        for j in range(1, star + 1):
            print("*", end="")

        print()

        if i <= n // 2:
            star -= 1
            space += 2
        else:
            star += 1
            space -= 2


# 4. Optimized Solid Diamond
def solid_diamond_optimized(n):
    if n % 2 == 0:
        n += 1

    star = 1
    space = n // 2

    for i in range(1, n + 1):
        print(" " * space + "*" * star)

        if i <= n // 2:
            star += 2
            space -= 1
        else:
            star -= 2
            space += 1


# 5. Optimized Butterfly
def butterfly_optimized(n):
    if n % 2 == 0:
        n += 1

    star = n // 2
    space = 1

    for i in range(1, n + 1):
        print("*" * star + " " * space + "*" * star)

        if i <= n // 2:
            star -= 1
            space += 2
        else:
            star += 1
            space -= 2




# Main Menu
def main():
    print("1. Solid Diamond")
    print("2. Hollow Diamond")
    print("3. Inverted Diamond / Butterfly")
    print("4. Optimized Solid Diamond")
    print("5. Optimized Butterfly")

    choice = int(input("ENTER YOUR CHOICE: "))
    n = int(input("ENTER NUMBER OF ROWS: "))

    if choice == 1:
        solid_diamond(n)
    elif choice == 2:
        hollow_diamond(n)
    elif choice == 3:
        inverted_diamond_butterfly(n)
    elif choice == 4:
        solid_diamond_optimized(n)
    elif choice == 5:
        butterfly_optimized(n)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
