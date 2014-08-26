#!python2
# Tui Popenoe
# Challenge47E.py - Caesar Cipher

from ast import literal_eval
from sys import argv

english = {
    0 : 'a',
    1 : 'b',
    2 : 'c',
    3 : 'd',
    4 : 'e',
    5 : 'f',
    6 : 'g',
    7 : 'h',
    8 : 'i',
    9: 'j',
    10: 'k',
    11: 'l',
    12: 'm',
    13: 'n',
    14: 'o',
    15: 'p',
    16: 'q',
    17: 'r',
    18: 's',
    19: 't',
    20: 'u',
    21: 'v',
    22: 'w',
    23: 'x',
    24: 'y',
    25: 'z'
}

cipher = {
     'a': 0 ,
     'b': 1 ,
     'c': 2 ,
     'd': 3 ,
     'e': 4 ,
     'f': 5 ,
     'g': 6 ,
     'h': 7 ,
     'i': 8 ,
     'j': 9 ,
     'k': 10,
     'l': 11,
     'm': 12,
     'n': 13,
     'o': 14,
     'p': 15,
     'q': 16,
     'r': 17,
     's': 18,
     't': 19,
     'u': 20,
     'v': 21,
     'w': 22,
     'x': 23,
     'y': 24,
     'z': 25
}



def caesar_cipher(lst, shift, alphabet=english):
    lst = list(lst)
    l = len(alphabet)
    for i in range(len(lst)):
        temp = cipher[lst[i]]
        lst[i] = alphabet[(temp + shift) % l]
    return ''.join(lst)

def main():
    if len(argv) > 1:
        print(caesar_cipher(argv[1], int(argv[2])))
    else:
        print(caesar_cipher(
            literal_eval(raw_input("Enter a phrase to dicipher: ")),
            int(raw_input("Enter a value to shift by: ")),
            english))

if __name__ == '__main__':
    main()
