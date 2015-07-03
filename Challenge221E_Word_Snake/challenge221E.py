#!/usr/bin/env python
# Tui Popenoe
# challenge221E.py  Word Snake

from sys import argv

def word_snake(lst):
    if lst:
        print(lst[0])
        space_length = len(lst[0]) - 1
        turn = False
        down = True
        for word in lst[1:]:
            if not turn and space_length + len(word) > 80:
                turn = True
            if turn and space_length - len(word) < 0:
                turn = False
            if not down:
                if not turn:
                    print('%s%s' % (' ' * space_length, word))
                    space_length += len(word) - 1
                else:
                    space_length -= len(word) - 1
                    print('%s%s' % (' ' * space_length, word[::-1]))
                down = True
            else:
                for letter in word[1:-1]:
                    print('%s%s' % (' ' * space_length, letter))
                down = False

def main():
    if len(argv) > 1:
        word_snake(argv[1:])
    else:
        word_snake(raw_input('Enter a list of words: ').split())

if __name__ == '__main__':
    main()