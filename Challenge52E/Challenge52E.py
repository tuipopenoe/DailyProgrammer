#!python2
# Tui Popenoe
# Exercise52E.py - Letter Value Sort

from sys import argv

alphabet = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9,
    'j' : 10,
    'k' : 11,
    'l' : 12,
    'm' : 13,
    'n' : 14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'w' : 23,
    'x' : 24,
    'y' : 25,
    'z' : 26
}

def positional_sort(lst):
    output = list()
    for i in lst:
        i = i.lower()
    for i in lst:
        word = []
        for j in i:
            word.append(alphabet.get(j))
        output.append(word)
    sorted_output = sorted(output, key=sum)
    sorted_output_words = list()
    del output[:]
    for i in sorted_output:
        word = []
        for j in i:
            for key, value in alphabet.iteritems():
                if j == value:
                    word.append(key)
        sorted_output_words.append(''.join(word))
    return sorted_output_words

def main():
    if len(argv) > 1:
        filename = argv[1]
    else:
        filename = raw_input()
    with open(filename, 'r') as f:
        lst = f.read().split()
        print positional_sort(lst)

if __name__ == '__main__':
    main()
