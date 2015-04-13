#!/usr/bin/env python
# Tui Popenoe
# Challenge210 E - Int Harmony

from sys import argv

def convert_to_binary_string(x):
    return '{0:08b}'.format(x)

def convert_to_int_string(x):
    return str(int(x, 2))

def compare_binary_ints(x, y):
    return [z for i, z in enumerate(x) if x[i] == y[i]]

def percent_compatible(x):
    return (float(len(x)) / 8.0) * 100

def invert_binary(x):
    return ''.join(['0' if z == '1' else '1' for z in x])

def int_harmony(x, y):
    x = convert_to_binary_string(x)
    y = convert_to_binary_string(y)
    compatible = percent_compatible(compare_binary_ints(x, y))
    print('%s%s' % (compatible,'% Compatible'))
    print('%s should avoid %s' % (convert_to_int_string(x),
                                  convert_to_int_string(invert_binary(x))))
    print('%s should avoid %s' % (convert_to_int_string(y),
                                  convert_to_int_string(invert_binary(y))))

def main():
    if len(argv) > 1:
        int_harmony(int(argv[1]), int(argv[2]))
    else:
        int_harmony(int(raw_input()), int(raw_input()))

if __name__ == '__main__':
    main()