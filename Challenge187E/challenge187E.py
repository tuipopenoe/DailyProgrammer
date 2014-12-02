#!python2
# Tui Popenoe
# challenge187E.py - A Flagon of Flags

from sys import argv

def read_flags(filename):
    flags = {}
    output = []
    with open(filename, 'r') as f:
        num_flags = int(f.readline().strip())
        for i in range(num_flags):
            flag = f.readline().strip().split(':')
            flags[flag[0]] = flag[1]
        inp = f.readline().strip().split()
        for i in inp:
            # Check longform first
            if i[0:2] == '--':
                output.append('flag: ' + i[2:])
            # Check shortform, loop through combined arguments
            elif i[0:1] == '-':
                for j in i[1:]:
                    output.append('flag: ' + flags[j])
            # Otherwise is an argument
            else:
                output.append('parameter: ' + i)
    return '\n'.join(output)

def main():
    if len(argv) > 1:
        print(read_flags(argv[1]))
    else:
        print(read_flags(raw_input('Enter an input file: ')))

if __name__ == '__main__':
    main()