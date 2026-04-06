"""
Special Shapes Collection

1. Heart Shape: A fixed 6x7 mathematical coordinate plot.
"""

# -------- Basic Approach --------

def heart_shape():
    """
    Pattern 14: Heart Shape
    Uses specific coordinate math for a 6x7 grid.
    """
    print("\nTHE HEART SHAPE:")
    for i in range(6):
        for j in range(7):
            # Modular logic for the top humps and linear equations for the bottom V
            condition = (
                (i == 0 and j % 3 != 0) or 
                (i == 1 and j % 3 == 0) or 
                (i - j == 2) or 
                (i + j == 8)
            )
            
            if condition:
                print(" * ", end="")
            else:
                print("   ", end="")
        print()


# -------- Optimized Approach --------
# Improvement: Using list comprehension for row generation.

def heart_shape_optimized():
    """Optimized version using join and list comprehension"""
    print("\nTHE HEART SHAPE (OPTIMIZED):")
    for i in range(6):
        # Build the row as a list, then join into a single string for printing
        row = [" * " if (i == 0 and j % 3 != 0) or 
                        (i == 1 and j % 3 == 0) or 
                        (i - j == 2) or 
                        (i + j == 8) 
               else "   " for j in range(7)]
        print("".join(row))


# -------- Main Execution with Try-Catch --------

def main():
    print("--- SPECIAL SHAPES MENU ---")
    print("1. Heart Shape (Basic)")
    print("2. Heart Shape (Optimized)")
    
    try:
        choice = int(input("\nENTER YOUR CHOICE: "))
        
        if choice == 1:
            heart_shape()
        elif choice == 2:
            heart_shape_optimized()
        else:
            print("INVALID CHOICE! PLEASE SELECT 1 OR 2.")
            
    except ValueError:
        # This catches errors if the user enters a string instead of an integer
        print("CRITICAL ERROR: Invalid Input! Please enter a numeric value.")
    except Exception as e:
        # General catch-all for any other unexpected errors
        print(f"AN UNEXPECTED ERROR OCCURRED: {e}")

if __name__ == "__main__":
    main()