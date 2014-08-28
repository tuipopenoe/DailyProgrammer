#!python
# Tui Popenoe
# Challenge26E.python

from sys import argv

def deduplicate(string):
    output = []
    for i in range(len(string)):
        if string[i-1] != string[i]:
            output += string[i]
        else:
            pass
    return ''.join(output)

def main():
    if len(argv) > 1:
        print(deduplicate(argv[1]))
    else:
        print(deduplicate(raw_input()))

if __name__ == '__main__':
    main()