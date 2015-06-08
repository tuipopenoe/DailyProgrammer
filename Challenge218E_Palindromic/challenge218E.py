#!/usr/bin/env python
#Tui Popenoe
# Challenge 218E.py -Palindromic Numbers

from sys import argv

def palindromicize(in_str):
    """Make the input number palindromic."""
    orig = in_str
    count = 0
    while not is_palindrome(in_str):
        temp = in_str
        in_str = str(int(temp) + int(temp[::-1]))
        count += 1
    print("%s gets palindromic after %s steps: %s" % (orig, count, in_str))
    return in_str

def is_palindrome(word):
    return word == word[::-1]

def test_palindromicize():
    assert palindromicize('24') == '66'
    assert palindromicize('28') == '121'


def main():
    # test_palindromicize()
    if len(argv) > 1:
        palindromicize(argv[1])
    else:
        palindromicize(raw_input("Enter a number to palindromicize: "))

if __name__ == '__main__':
    main()
