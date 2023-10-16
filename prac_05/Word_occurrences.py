"""
Word Occurrences
Estimate: 25 minutes
Actual:   20 minutes
"""


def main():
    """Get user input and display word counts."""
    user_input = input("Enter a string: ")
    counts = word_count(user_input)
    print_word_counts(counts)


def word_count(text):
    """Count occurrences of words in a given text."""
    words = text.split()
    word_counts = {}

    for word in words:
        word = word.strip('.,!?"\'').lower()
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_word_counts(word_counts):
    """Print word counts in a sorted and aligned format."""
    max_word_length = max(len(word) for word in word_counts)

    for word, count in sorted(word_counts.items()):
        print(f"{word:>{max_word_length}} : {count}")


main()
