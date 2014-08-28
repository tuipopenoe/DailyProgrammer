#!python2
# Tui Popenoe
# Challenge32E.py - Base 26 Multiplication

from sys import argv

values = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7,
    'i' : 8,
    'j' : 9,
    'k' : 10,
    'l' : 11,
    'm' : 12,
    'n' : 13,
    'o' : 14,
    'p' : 15,
    'q' : 16,
    'r' : 17,
    's' : 18,
    't' : 19,
    'u' : 20,
    'v' : 21,
    'w' : 22,
    'x' : 23,
    'y' : 24,
    'z' : 25
}

letters = {
    0  : 'a',
    1  : 'b',
    2  : 'c',
    3  : 'd',
    4  : 'e',
    5  : 'f',
    6  : 'g',
    7  : 'h',
    8  : 'i',
    9  : 'j',
    10 : 'k',
    11 : 'l',
    12 : 'm',
    13 : 'n',
    14 : 'o',
    15 : 'p',
    16 : 'q',
    17 : 'r',
    18 : 's',
    19 : 't',
    20 : 'u',
    21 : 'v',
    22 : 'w',
    23 : 'x',
    24 : 'y',
    25 : 'z'
}

def base_twenty_six_multiply(num1, num2):
    num1, num2 = num1.lower(), num2.lower
    val1 = []
    val2 = []
    output = []
    for i in num1:
        val1.append(values[i])
    val1 = int(''.join(map(str,val1)))
    for i in num2:
        val2.append(values[i])
    val2 = int(''.join(map(str, val2)))
    val3 = val1 * val2
    val3 = str(val3)
    for i in val3:
        output.append(letters[int(i)])
    return ''.join(output)

def main():
    if len(argv) > 1:
        print(base_twenty_six_multiply(argv[1], argv[2]))
    else:
        print(base_twenty_six_multiply(raw_input(), raw_input()))

if __name__ == '__main__':
    main()