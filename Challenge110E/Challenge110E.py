#!python2
# Tui Popenoe
# Challenge110E.py - Keyboard Shift

import sys

keys = {
    'a' : 'a',
    'b' : 'v',
    'c' : 'x',
    'd' : 's',
    'e' : 'w',
    'f' : 'd',
    'g' : 'f',
    'h' : 'g',
    'i' : 'u',
    'j' : 'h',
    'k' : 'j',
    'l' : 'k',
    'm' : 'n',
    'n' : 'b',
    'o' : 'i',
    'p' : 'o',
    'q' : 'q',
    'r' : 'e',
    's' : 'a',
    't' : 'r',
    'u' : 'y',
    'v' : 'c',
    'w' : 'q',
    'x' : 'z',
    'y' : 't',
    'z' : 'z',
    '[' : 'p',
    '{' : 'P',
    ';' : 'l',
    ':' : 'L',
    ',' : 'm',
    '<' : 'M',
    ' ' : ' '
}

def shift(string):
    output = list()
    for i in string:
        for k,v in keys.iteritems():
            if i == k:
                output.append(v)
            elif i == k.upper():
                output.append(v.upper())
            

    print(''.join(output))
    return output

def main():
    if len(sys.argv) > 1:
        shift(sys.argv[1])
    else:
        shift(raw_input('Enter a string to shift: '))

if __name__=='__main__':
    main()
