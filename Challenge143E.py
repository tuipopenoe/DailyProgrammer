# Tui Popenoe
# Challenge 143 E - Braille

import sys

def convertBraile(inputfile):
    f = open(inputfile, 'r')
    lst = f.readlines().split()
    output = list()
    print(lst)

    for i in len(lst):
        output[i%6].append(lst[i])



def main():


if __name__=='__main__':
    main()

dictionary = {
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h' : 'O.OO..',
    'i' : '.OO...',
    'j' : '.OOO..',
    'k' : 'O...O.',
    'l' : 'O.O.O.',
    'm' : 'OO..O.',
    'n' : 'OO.OO.',
    'o' : 'O..OO.',
    'p' : 'OOO.O.',
    'q' : 'OOOOO.',
    'r' : 'O.OOO.',
    's' : '.OO.O.',
    't' : '.OOOO.',
    'u' : 'O...OO',
    'v' : 'O.O.OO',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO'
}