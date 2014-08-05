# Tui Popenoe
# Challenge 162 Novel Compression, pt. 1

""" Implementation of a compression algorithm. Accepts input as a file or 
    arguments from the command line. 

    Rules:
    1.) If the chunk is just a number (eg. 37), word number 37 from 
    the dictionary (zero-indexed, so 0 is the 1st word) is printed lower-case.
    2.) If the chunk is a number followed by a caret (eg. 37^), then word 37 
    from  the dictionary will be printed lower-case, with the first letter 
    capitalised.
    3.) If the chunk is a number followed by an exclamation point (eg. 37!), 
    then word 37 from the dictionary will be printed upper-case.
    4.) If it's a hyphen (-), then instead of putting a space in-between the 
    previous and next words, put a hyphen instead.
    5.) If it's any of the following symbols: . , ? ! ; :, then put that 
    symbol at the end of the previous outputted word.
    6.) If it's a letter R (upper or lower), print a new line.
    7.) If it's a letter E (upper or lower), the end of input has been reached.
"""

import sys

def getInput(filename='input.txt'):
    f = open(filename, 'r')
    dictionary = list()
    compressedText = list()

    n = int(f.readline())

    for i in range(n):
        dictionary.append(f.readline())

    compressedText.append(f.readlines().split())

    f.close()

    return [dictionary, compressedText]

def decompress(dictionary, text):
    output = list()
    for line in text:
        for word in line:
            if isinstance(word, int):
                output.append(dictionary[word])
            elif word[-1] == '^':
                output.append(dictionary[word[:-1]].capitalize())
            elif word[-1] == '!':
                output.append(dictionary[word[:-1].upper()])
            elif word == '-':
                output.append(word)
            elif word == '.' or word == ',' or word == '?' or word == '!' or \
                word == '.' or word == ',':
                output.append(word)
            elif word == 'R' or word == 'r':
                output.append('\n')
            elif word == 'E' or word == 'e':
                printDecyptedText(output)

def printDecryptedText(output):
    print(''.join(output))

def main():
    inputs = getInput(sys.argv[1])
    decompress(inputs[0], inputs[1])