# Tui Popenoe
# Challenge 143 E - Braille

import sys

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
    'w' : '.OOO.O',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO'
}

def convertBraile(inputfile, length, dictionary):
    f = open(inputfile, 'r')
    lst = f.read().split()
    output = [''] * length
    print(lst)

    for i in range(len(lst)):
        output[i%length] += lst[i]
    print(output)

    message = ''

    for j in output:
        for letter, braille in dictionary.iteritems():
            if braille == j:
                message += letter

    print message

def main():
     convertBraile(sys.argv[1], int(sys.argv[2]), dictionary)

if __name__=='__main__':
    main()