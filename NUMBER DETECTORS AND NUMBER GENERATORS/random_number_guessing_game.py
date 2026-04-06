"""
Number Guessing Game

This program implements a simple number guessing game where the user
attempts to guess a randomly generated number within a limited number of attempts.

Game Rules:
- The system generates a random number between 1 and 10.
- The user is given 3 chances to guess the number.
- Each correct guess awards 10 points.
- Maximum possible score is 30.

"""

# -------- Basic Approach --------

import random

def main():
    try:
        name = input("ENTER YOUR NAME: ")
    except EOFError:
        print("ERROR READING INPUT")
        return

    num = int(random.random() * 10 + 1)
    score = 0

    for i in range(3, 0, -1):
        print("GUESS ANY NUMBER BETWEEN 1-10, YOU HAVE 3 CHANCES")
        try:
            guess = int(input())
        except ValueError:
            print("INVALID INPUT! PLEASE ENTER A NUMBER.")
            continue
        except EOFError:
            print("ERROR READING INPUT")
            continue

        if guess == num:
            print("CORRECT GUESS!! 10 POINTS TO YOU")
            score += 10
            num = random.randint(1, 10)
        else:
            print(f"WRONG GUESS!! YOU HAVE {i-1} CHANCES MORE")

    print(f"{name} YOUR SCORE IS : {score} OUT OF 30")


if __name__ == "__main__":
    main()


# -------- Optimized & Corrected Approach --------
# Fixes:
# - Correct comparison (guess vs num)
# - Uses randint for clarity
# - Cleaner game flow

import random

def play_game():
    try:
        name = input("ENTER YOUR NAME: ")
    except EOFError:
        print("ERROR READING INPUT")
        return

    score = 0

    for i in range(3, 0, -1):
        num = random.randint(1, 10)
        print("GUESS ANY NUMBER BETWEEN 1-10")

        try:
            guess = int(input())
        except ValueError:
            print("INVALID INPUT! PLEASE ENTER A NUMBER.")
            print(f"YOU HAVE {i-1} CHANCES MORE")
            continue
        except EOFError:
            print("ERROR READING INPUT")
            continue

        if guess == num:
            print("CORRECT GUESS!! 10 POINTS TO YOU")
            score += 10
        else:
            print(f"WRONG GUESS!! NUMBER WAS {num}. YOU HAVE {i-1} CHANCES MORE")

    print(f"{name} YOUR SCORE IS : {score} OUT OF 30")


if __name__ == "__main__":
    play_game()