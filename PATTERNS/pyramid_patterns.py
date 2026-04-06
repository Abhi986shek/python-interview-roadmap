"""
Pyramid and Hollow Pyramid Patterns

1. Full Pyramid (Stars)
2. Inverted Full Pyramid (Stars)
3. Hollow Pyramid (Outline only)
4. Hollow Inverted Pyramid (Outline only)
5. Character-Number Inverted Hollow Pyramid (Letters on border, numbers inside)
6. Palindromic Number Pyramid (12321 style)
"""

# -------- Basic Approaches --------

def full_pyramid(n):
    star = 1
    space = n - 1
    for i in range(1, n + 1):
        for j in range(space):
            print(" ", end="")
        for j in range(star):
            print("*", end="")
        star += 2
        space -= 1
        print()

def inverted_pyramid(n):
    star = 2 * n - 1
    space = 0
    for i in range(n, 0, -1):
        for j in range(space):
            print(" ", end="")
        for j in range(star):
            print("*", end="")
        star -= 2
        space += 1
        print()

def hollow_pyramid(n):
    space = n - 1
    star = 1
    for i in range(1, n + 1):
        for j in range(space):
            print(" ", end="")
        for j in range(1, star + 1):
            if j == 1 or j == star or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        star += 2
        space -= 1
        print()

def hollow_inverted_pyramid(n):
    space = 0
    star = 2 * n - 1
    for i in range(1, n + 1):
        for j in range(space):
            print(" ", end="")
        for j in range(1, star + 1):
            if j == 1 or j == star or i == 1:
                print("*", end="")
            else:
                print(" ", end="")
        star -= 2
        space += 1
        print()

def char_num_inverted_hollow(n):
    star = 2 * n - 1
    space = 0
    letter_code = ord('A')
    num = 1
    for i in range(1, n + 1):
        for j in range(space):
            print(" ", end="")
        for j in range(1, star + 1):
            if i == 1 or j == 1 or j == star:
                print(chr(letter_code), end="")
                letter_code += 1
            else:
                print(num, end="")
                num += 1
        star -= 2
        space += 1
        print()

def palindromic_number_pyramid(n):
    star = 1
    space = n - 1
    for i in range(1, n + 1):
        # Print spaces
        for j in range(space):
            print(" ", end="")
        # Print numbers
        k = i
        for j in range(1, star + 1):
            if j > i:
                k -= 1
                print(k, end="")
            else:
                print(j, end="")
        star += 2
        space -= 1
        print()

# -------- Optimized Approaches --------
# Improvements:
# - Use string multiplication for padding and star repetition.
# - Use join and list slicing for palindromic number sequences.

def full_pyramid_opt(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def palindromic_opt(n):
    for i in range(1, n + 1):
        left = "".join(str(x) for x in range(1, i + 1))
        right = left[-2::-1] # Slice to get everything except last char, then reverse
        print(" " * (n - i) + left + right)

# -------- Main Execution --------

def main():
    print("--- PYRAMID PATTERNS MENU ---")
    print("1. Full Pyramid")
    print("2. Inverted Pyramid")
    print("3. Hollow Pyramid")
    print("4. Hollow Inverted Pyramid")
    print("5. Char-Number Hollow Inverted")
    print("6. Palindromic Number Pyramid")
    
    try:
        choice = int(input("\nSELECT CHOICE (1-6): "))
        rows = int(input("ENTER NUMBER OF ROWS: "))
        
        if choice == 1: full_pyramid(rows)
        elif choice == 2: inverted_pyramid(rows)
        elif choice == 3: hollow_pyramid(rows)
        elif choice == 4: hollow_inverted_pyramid(rows)
        elif choice == 5: char_num_inverted_hollow(rows)
        elif choice == 6: palindromic_number_pyramid(rows)
        else: print("Invalid Choice.")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()