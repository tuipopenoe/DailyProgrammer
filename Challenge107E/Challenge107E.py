# Tui Popenoe
# Challenge107E.py All Possible Decodings

import sys

code = {
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

def allDecodings(string, output):
    for i in range(0, len(string)-1, 2):
        if string[i] == 1 or string[i] == 2:
            output.append(string[i])
            output.append(string[i+1])
            output.append(allDecodings(string[i:], output))
            output.append(string[i] + string[i+1])
        else:
            output.append(string[i] + string[i+1])
            output.append(allDecodings(string[i+1:], output))
    return output

def main():
    if len(sys.argv) > 1:
        print(allDecodings(sys.argv[1], list()))
    else:
        print(allDecodings(raw_input(), list()))

if __name__=='__main__':
    main()
