#!/usr/bin/env python
# Tui Popenoe
# Shuffling a list

import random
from sys import argv


def shuffle(lst):
    if not isinstance(lst, list):
        try:
            lst = list(lst)
        except:
            raise Exception('Incorrectly formatted list')
    shuffled_lst = []
    while len(lst) > 0:
        r = random.randint(0, len(lst) -1)
        shuffled_lst.append(lst[r])
        del lst[r]
    return shuffled_lst

def test_shuffle():
    test_1 = shuffle('hello world')
    assert test_1 != 'hello world'

def main():
    if len(argv) > 1:
        print(shuffled_lst(argv[1:])
    else:
        print(shuffled_lst(raw_input('Enter a lst to shuffle: ')))

if __name__ == '__main__':
    main()
