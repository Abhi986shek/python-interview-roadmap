"""
Diamond Pattern Collection - Version 2.0
Includes: Solid, Hollow, Butterfly, and the missing Hollow Diamond in Stars (Pattern 32).
"""

# -------- Basic Approaches --------

def solid_diamond(n):
    if n % 2 == 0: n += 1
    space = n // 2
    star = 1
    for i in range(1, n + 1):
        print("  " * space + " *" * star)
        if i <= n // 2:
            star += 2
            space -= 1
        else:
            star -= 2
            space += 1

def hollow_diamond(n):
    if n % 2 == 0: n += 1
    space = n // 2
    star = 1
    for i in range(1, n + 1):
        print(" " * space, end="")
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

def inverted_diamond_butterfly(n):
    """Option 3: Stars on the outside, space grows then shrinks in middle"""
    if n % 2 == 0: n += 1
    space = 1
    outer_stars = n // 2
    for i in range(1, n + 1):
        print("*" * outer_stars + " " * space + "*" * outer_stars)
        if i <= n // 2:
            space += 2
            outer_stars -= 1
        else:
            space -= 2
            outer_stars += 1

def hollow_diamond_in_stars(n):
    """
    A solid block of stars with a diamond hole.
    Logic: Top-down and bottom-up triangles meeting in the middle.
    """
    if n % 2 == 0: n += 1
    
    # Top Half
    for i in range(n // 2 + 1, 0, -1):
        # Left stars + middle space + right stars
        print("*" * i + " " * (n - 2 * i + 2) + "*" * i)
    
    # Bottom Half
    for i in range(2, n // 2 + 2):
        print("*" * i + " " * (n - 2 * i + 2) + "*" * i)

# -------- Optimized Approaches --------

def solid_diamond_optimized(n):
    if n % 2 == 0: n += 1
    rows = [("*" * i).center(n) for i in range(1, n + 1, 2)]
    print("\n".join(rows + rows[-2::-1]))

def butterfly_optimized(n):
    if n % 2 == 0: n += 1
    rows = []
    for i in range(1, n + 1, 2):
        side = "*" * ((n - i) // 2)
        rows.append(side + " " * i + side)
    print("\n".join(rows + rows[-2::-1]))

# -------- Main Execution --------

def main():
    print("--- DIAMOND PATTERNS MENU ---")
    print("1. Solid Diamond")
    print("2. Hollow Diamond")
    print("3. Inverted Diamond (Butterfly)")
    print("4. [OPTIMIZED] Solid Diamond")
    print("5. [OPTIMIZED] Butterfly")
    print("6. Hollow Diamond in Stars") 
    
    try:
        choice = int(input("\nSELECT CHOICE (1-6): "))
        rows = int(input("ENTER NUMBER OF ROWS: "))
        print("\nRESULT:\n")
        
        if choice == 1: solid_diamond(rows)
        elif choice == 2: hollow_diamond(rows)
        elif choice == 3: inverted_diamond_butterfly(rows)
        elif choice == 4: solid_diamond_optimized(rows)
        elif choice == 5: butterfly_optimized(rows)
        elif choice == 6: hollow_diamond_in_stars(rows)
        else: print("Invalid Choice.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()