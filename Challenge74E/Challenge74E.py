# Tui Popenoe
# Challenge74E.def 

import math
import sys
from itertools import islice

def nearest(m):
    return (math.log(m * math.sqrt(5)) / (math.log((1 + math.sqrt(5))/2)))

def fibonacci(a=0, b=1):
    yield a
    while True:
        yield b
        a, b = b, a + b

def zeckendorf(n):
    output = list()
    m = nearest(n)
    f = list(islice(fibonacci(), m + 1))
    f.pop(0)
    f.reverse()
    for i in f:
        if i < n and (sum(output) + i) <= n:
            output.append(i)

    return output


def main():
    if len(sys.argv) == 2:
        print(zeckendorf(int(sys.argv[1])))
    else:
        print(zeckendorf(int(raw_input())))

if __name__ == '__main__':
    main()