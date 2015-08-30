#!/usr/bin/env python
# Tui Popenoe
# challenge228E.py - Letters in Alphabetical Order


from sys import argv
import re, string


letters = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}


def in_order(word):
    """Determine if all the letters in a word are in alphabetical order.
    Return True if all are in order, False otherwise."""
    for i in range(len(word) - 1):
        if letters[word[i+1]] < letters[word[i]]:
            return False
    return True


def in_reverse_order(word):
    """Determine if all the letters in a word are in reverse alphabetical
    order. Return True if all letters are in reverse order, False otherwise"""
    for i in range(len(word) - 1):
        if letters[word[i+1]] > letters[word[i]]:
            return False
    return True


def analyze_words(filename=None):
    """Analyze the words in the provided input, printing to the consol if
    the word is in order alphabetically, not in order, or in reverse order."""
    if not filename:
        filename = 'input.txt'
    with open(filename) as f:
        words = f.readlines()
        for i in words:
            i = remove_invalid_chars(i)
            if in_order(i):
                print('%s IN ORDER'  % i)
            elif in_reverse_order(i):
                print('%s REVERSE ORDER' % i)
            else:
                print('%s NOT IN ORDER' % i)


def remove_invalid_chars(word):
    """Remove all non-letter characters from word and convert to .lower"""
    word = re.sub(r'\W+', '', word).lower()
    return word


def main():
    if len(argv) > 1:
        analyze_words(argv[1:])
    else:
        filename = raw_input('Enter a filename to analyze: ')
        if not filename:
            filename = None
        analyze_words(filename)


def test_remove_invalid_chars():
    """Test the remove_invalid_chars method."""
    raise NotImplementedError()


def test_analyze_words():
    """Test the analyze_words() methods."""
    raise NotImplementedError()

if __name__ == '__main__':
    main()
