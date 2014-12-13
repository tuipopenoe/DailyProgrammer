#!python2
# Tui Popenoe
# challenge191E.py - Word Counting

import sys

def count_words(filename):
    """Return a count of the words in a file."""
    with open(filename, 'r') as f:
        word_count = {}
        words = f.read().split()
        for word in words:
            word_count[word] += 1
        return word_count

def main():
    if len(sys.argv) > 1:
        print(count_words(sys.argv[1]))
    else:
        print(count_words(raw_input("Enter a file to count the words: ")))

if __name__ == '__main__':
    main()