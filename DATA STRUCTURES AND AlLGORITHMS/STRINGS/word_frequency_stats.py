"""
Calculates the frequency of each word in a string and identifies 
the words with the maximum and minimum occurrences.
"""
tfrom collections import Counter

try:
    user_input = input("ENTER THE STRING\n").strip()

    if not user_input:
        raise ValueError("String cannot be empty.")

    words = user_input.split()

    word_counts = Counter(words)

    for word, count in word_counts.items():
        print(f"{word} count is = {count}")

    min_word = min(word_counts, key=word_counts.get)
    max_word = max(word_counts, key=word_counts.get)

    print(f"{min_word} IS THE LOWEST OCCURRING WITH COUNT = {word_counts[min_word]}")
    print(f"{max_word} IS THE HIGHEST OCCURRING WITH COUNT = {word_counts[max_word]}")

except Exception as e:
    print(f"An error occurred: {e}")
