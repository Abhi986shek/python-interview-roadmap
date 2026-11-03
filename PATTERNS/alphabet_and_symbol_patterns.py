"""
Alphabet and Geometric Symbol Patterns

1. Shape 'I' 
2. Shape 'L' 
3. Shape 'E' 
4. Shape 'K' style / Fork 
5. X-Shape with Incrementing Letters 
6. Shape 'J' 
7. X-Shape with Stars 
8. Inverted Hollow V / Pyramid 
9. Shape 'A' / Hollow Pyramid with Crossbar 
10. Shape 'P' 
"""

# -------- Basic Approaches --------

def shape_I(n):
    """Pattern 8: Horizontal top/bottom and vertical middle"""
    for i in range(1, n + 1):
        for j in range(1, n):
            if i == 1 or i == n or j == n // 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def shape_L(n):
    """Pattern 9: Vertical left and horizontal bottom"""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == n or j == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def shape_E(n):
    """Pattern 10: Left wall and three horizontal bars"""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or i == n // 2 + 1 or j == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def shape_K_fork(n):
    """Pattern 24: Left wall and diagonal strokes"""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i + j == n or i - j == n - 4 or j == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def x_shape_letters(n):
    """Pattern 27: X-shape using incrementing alphabet characters"""
    letter_code = ord('A')
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == i or j + i == n + 1:
                print(chr(letter_code), end="")
                letter_code += 1
            else:
                print("  ", end="")
        print()

def shape_J(n):
    """Pattern 28: Top bar, middle stem, and hooked bottom"""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            condition = (i == 1 or j == n // 2 + 1 or 
                        (i == n and j <= n // 2 + 1) or 
                        (i == n - 1 and j == 1))
            if condition:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def x_shape_stars(n):
    """Pattern 6: Simple X-shape with stars"""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == i or j + i == n + 1:
                print("*", end="")
            else:
                print("  ", end="")
        print()

def inverted_hollow_V(n):
    space = 0
    star = 2 * n - 1

    for i in range(1, n + 1):
        for j in range(1, space + 1):
            print(" ", end="")
        for j in range(1, star + 1):
            if j == 1 or j == star:
                print("*", end="")
            else:
                print(" ", end="")
        print()
        space += 1
        star -= 2

def shape_A(n):
    space = n - 1
    star = 1
    for i in range(1, n + 1):
        for j in range(1, space + 1):
            print(" ", end="")

        for j in range(1, star + 1):
            if j == 1 or j == star or i == n // 2 + 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
        star += 2
        space -= 1

def shape_P(n):
    """Pattern 15: Left wall, top/middle bar, and right closure for top half"""
    for i in range(1, n + 2):
        for j in range(1, n + 1):
            if i == 1 or j == 1 or i == n // 2 + 1 or (i <= n // 2 and j == n):
                print("*", end="")
            else:
                print(" ", end="")
        print()

# -------- Main Execution --------

def main():
    print("--- ALPHABET & SYMBOL MENU ---")
    print("1. Shape I  2. Shape L  3. Shape E")
    print("4. Shape K  5. X-Letters 6. Shape J")
    print("7. X-Stars  8. Hollow V  9. Shape A")
    print("10. Shape P")
    
    try:
        choice = int(input("\nSELECT A PATTERN (1-10): "))
        rows = int(input("ENTER NUMBER OF ROWS: "))
        print("\nRESULT:\n")
        
        patterns = {
            1: shape_I, 2: shape_L, 3: shape_E, 4: shape_K_fork,
            5: x_shape_letters, 6: shape_J, 7: x_shape_stars,
            8: inverted_hollow_v, 9: shape_A, 10: shape_P
        }
        
        if choice in patterns:
            patterns[choice](rows)
        else:
            print("Invalid Choice.")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
