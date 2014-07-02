# Tui Popenoe
# Challenge 146 Polygon Perimeter

import math
import sys

def perimeter(n, r):
    s = float(r) * 2 * math.sin(math.pi / float(n))


    print(s * float(n))
    return s * float(n)

def main():
    perimeter(sys.argv[1], sys.argv[2])

if __name__=='__main__':
    main()