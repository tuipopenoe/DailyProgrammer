#!python2
# Tui Popenoe
# Challenge56E.py - ABACABA Sequence

from sys import argv

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def abacaba(n):
    lst = ['a']
    for i in range(1, n):
        word = lst[i-1] + alphabet[i] + lst[i-1]
        lst.append(word)
    #print(lst)
    return lst

def main():
    if len(argv) == 2:
        abacaba(int(argv[1]))
    else:
        abacaba(int(raw_input("Enter an integer between 1 and 26: ")))

if __name__ == '__main__':
    main()