#!/usr/bin/env python
# Tui Popenoe
# Challenge236E - Random Bag System

from random import randint
from sys import argv

def create_bag():
    return ['O', 'I', 'S', 'Z', 'L', 'J', 'T']

def choose_random(lst):
    if lst:
        return lst.pop(randint(0, len(lst) -1))

def random_bag(num):
    bag = []
    output = []
    for i in range(num):
        if not bag:
            bag = create_bag()
        output.append(choose_random(bag))
    return ''.join(output)

def main():
    if len(argv) > 1:
        print(random_bag(int(''.join(argv[1:]))))
    else:
        print(random_bag(int(raw_input("Enter a number of tetrominos: "))))


def test_random_bag():
    for i in range(50):
        x = random_bag(50)
        for i in range(len(x) -2):
            y = x[i:i+3]
            assert not (y[0] == y[1] == y[2])


if __name__ == '__main__':
    main()
    test_random_bag()
