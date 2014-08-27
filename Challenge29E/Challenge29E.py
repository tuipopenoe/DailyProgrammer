#!python2
# Tui Popenoe
# Challenge29E.py - Palindrome

from sys import argv

def is_palindrom(string):
    mod = len(string) % 2
    if string[:len(string)/2] == (string[len(string)/2+mod:])[::-1]:
        return True
    else:
        return False

def main():
    if len(argv) > 1:
        print(is_palindrom(argv[1]))
    else:
        print(is_palindrom(raw_input()))

if __name__ == '__main__':
    main()