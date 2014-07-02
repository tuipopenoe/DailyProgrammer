# Tui Popenoe
# Challenge 145 Tree Generation

import sys

def createTree(m, trunk, leaf):
    n = int(m)
    air = ''
    body = ''
    under = ((n-3) /2) * ' '
    for i in range(1, n+1, 2):
        air = ' ' * ((n-i) /2)
        leaves = leaf * i
        print(air + leaves + air)
    print(under + trunk*3 + under)

def main():
    createTree(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == '__main__':
    main()