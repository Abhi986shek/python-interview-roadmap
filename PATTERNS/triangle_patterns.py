"""
Comprehensive Triangle and Border Patterns 

"""

# -------- 1. Star Triangles (Solid & Mirrored) --------

def right_angled_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

def inverted_right_angled_triangle(n):
    for i in range(n, 0, -1):
        print("*" * i)

def mirrored_right_angled_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)

# -------- 2. Hollow Triangles & Diagonals --------

def hollow_triangle_bottom_base(n):
    """Original Option 4"""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == 1 or j == i or i == n:
                print("*", end=" ")
            else:
                print("  ", end="")
        print()

def hollow_triangle_top_base(n):
    """Original Option 5"""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == 1 or i + j == n + 1 or i == 1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

def hollow_mirrored_right_triangle(n):
    """Original Option 6: Right wall, top, main diagonal"""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == i or j == n or i == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def hollow_inverted_mirrored_right_triangle(n):
    """Original Option 7: Right wall, bottom, anti-diagonal"""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i + j == n + 1 or j == n or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def hollow_inverted_right(n):
    """Left wall, top, hypotenuse"""
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            if i == n or j == 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def hollow_mirrored_bottom_right(n):
    """Right wall, bottom, hypotenuse"""
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            if i == n or j == 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# -------- 3. Number Triangles (Sequential & Snake) --------

def sequential_number_triangle(n):
    """Original Option 8"""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def incrementing_row_triangle(n):
    """Original Option 9"""
    start_val = 0
    for i in range(1, n + 1):
        for j in range(1 + start_val, i + start_val + 1):
            print(j, end="")
        start_val += 1
        print()

def snake_number_triangle(n):
    """Original Option 10"""
    current = 1
    for i in range(1, n + 1):
        row = list(range(current, current + i))
        if i % 2 == 0: row = row[::-1]
        print(*(f"{num:<3}" for num in row))
        current += i

def snake_triangle_optimized(n):
    """Original Option 11"""
    # This uses the high-performance list comprehension approach
    current = 1
    for i in range(1, n + 1):
        nums = [str(x) for x in range(current, current + i)]
        if i % 2 == 0: nums.reverse()
        print(" ".join(nums))
        current += i

# -------- Main Execution --------

def main():
    print("--- FULL PATTERN SELECTION MENU (13 OPTIONS) ---")
    print("1. Solid Right-Angled")
    print("2. Solid Inverted Right")
    print("3. Solid Mirrored Right")
    print("4. Hollow Right (Bottom Base)")
    print("5. Hollow Right (Top Base)")
    print("6. Hollow Mirrored (Diagonal/Top)")
    print("7. Hollow Inverted Mirrored (Diagonal/Bottom)")
    print("8. Sequential Number Triangle")
    print("9. Incrementing Row Triangle")
    print("10. Snake Number Triangle")
    print("11. [OPTIMIZED] Snake Triangle")
    print("12. Hollow Inverted Right")
    print("13. Hollow Mirrored Right (Bottom Base)")
    
    try:
        choice = int(input("\nENTER YOUR CHOICE (1-13): "))
        rows = int(input("ENTER THE NUMBER OF ROWS: "))
        print("\nRESULT:\n")

        patterns = {
            1: right_angled_triangle, 2: inverted_right_angled_triangle,
            3: mirrored_right_angled_triangle, 4: hollow_triangle_bottom_base,
            5: hollow_triangle_top_base, 6: hollow_mirrored_right_triangle,
            7: hollow_inverted_mirrored_right_triangle, 8: sequential_number_triangle,
            9: incrementing_row_triangle, 10: snake_number_triangle,
            11: snake_triangle_optimized, 12: hollow_inverted_right,
            13: hollow_mirrored_bottom_right
        }

        if choice in patterns:
            patterns[choice](rows)
        else:
            print("INVALID CHOICE selected.")
        
    except ValueError:
        print("ERROR: Please enter valid integers.")

if __name__ == "__main__":
    main()