# Tui Popenoe
# Challenge122E.py - Words with Ordered Vowels

import sys

def orderedVowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    print(string)
    for i in string:
        if len(vowels) == 0:
            return True
        if i.lower() == vowels[0]:
            vowels.pop(0)

    if len(vowels) == 0:
        return True
    return False

def main():
    ordered = list()
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')
        lst = f.read().split()
        for i in lst:
            if orderedVowels(i):
                ordered.append(i)
    else:
        f = open(raw_input(), 'r')
        lst = f.read().split()
        for i in lst:
            if orderedVowels(i):
                ordered.append(i)
    print("Words with Ordered Vowels: ")
    print(ordered)
    return ordered

if __name__ == '__main__':
    main()