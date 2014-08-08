# Tui Popenoe
# Challenge79E.py - Counting in Steps

""" A function that returns a list containing the step elements counting from
a to b in steps of equal size. """

import sys


def step_count(a, b, steps):
    step = (b - a) / (steps - 1)
    print(step)
    output = list()
    for i in range(steps):
        output.append(a + (step * i))
    return output


def main():
    if len(sys.argv) > 1:
        print(step_count(float(sys.argv[1]), float(sys.argv[2]),
              int(sys.argv[3])))
    else:
        pass

if __name__ == '__main__':
    main()
