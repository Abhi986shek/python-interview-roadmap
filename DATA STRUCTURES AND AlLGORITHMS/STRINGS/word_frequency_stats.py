"""
Calculates the frequency of each word in a string and identifies 
the words with the maximum and minimum occurrences.
"""
try:
    user_input = input("ENTER THE STRING\n").strip()
    if not user_input:
        raise ValueError("String cannot be empty.")

    words = user_input.split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in word_counts.items():
        print(f"{word} count is = {count}")

    # Find min and max using built-in optimization
    min_word = min(word_counts, key=word_counts.get)
    max_word = max(word_counts, key=word_counts.get)

    print(f"{min_word} IS THE LOWEST ONE OCCURING WITH A COUNT OF ={word_counts[min_word]}")
    print(f"{max_word} IS THE HIGHEST ONE OCCURING WITH A COUNT OF ={word_counts[max_word]}")

except Exception as e:
    print(f"An error occurred: {e}")
