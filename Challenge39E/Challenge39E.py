#!python2
# Tui Popenoe
# Challenge39E.py - FizzBuzz

from sys import argv

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

def main():
    if len(argv) > 1:
        fizzbuzz(int(argv[1]))
    else:
        fizzbuzz(int(raw_input()))

if __name__ == '__main__':
    main()