# Tui Popenoe
# Challenge137E.py - String Transposition

"""Transpose the given string"""

def transpose():
    n = int(raw_input())
    strings = list()
    output = [''] * 256
    m = 0
    for i in range(n):
        strings.append(raw_input())

    for i in range(len(strings)):
        for j in range(len(strings[i])):
            output[j] += (strings[i][j])
        for j in range(256 - len(strings[i])):
            output[j] += ' '

    for i in strings:
        if len(i) > m:
            m = len(i)

    for i in range(m):
        if output[i] is not '':
            print(output[i])

def main():
    transpose()

if __name__=='__main__':
    main()