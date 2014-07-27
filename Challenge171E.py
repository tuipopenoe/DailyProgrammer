# Tui Popenoe
# Challenge171E.py - Hex to 8x8 Bitmap

import binascii
import sys

def hexToBinary(string):
    binary_string = binascii.unhexlify(string)
    print(binary_string)
    return binary_string

def drawImage(binaryString):
    for i in binaryString:
        if(i == 1):
            print("*")
        else:
            print(" ")

def main():
    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')
        l = f.readlines()
        for i in l:
            drawImage(hexToBinary(i))
    else:
        l = raw_input().split()
        for i in l:

            drawImage(hexToBinary(i))

if __name__=='__main__':
    main()