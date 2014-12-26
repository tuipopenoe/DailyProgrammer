# Tui Popenoe
# Challenge 149 Disemvoweler

import sys

def disemvowel(string):
    output = list()
    removed = list()
    vowels = ['a', 'e', 'i', 'o', 'u', ' ']
    for i in string:
        if i not in vowels:
            output.append(i)
        elif i in vowels[:-1]:
            removed.append(i)

    return [''.join(output), ''.join(removed)]

def main():
    if len(sys.argv) > 1:
        print(disemvowel(sys.argv[1]))
    else:
        print(disemvowel(raw_input('Enter a string to disemvowel: ')))

if __name__ == '__main__':
    main()