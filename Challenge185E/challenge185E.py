#!python2
# Tui Popenoe
# challenge185E.py - Generated Twitter Handles

from sys import argv

def find_handles(filename):
    output = []
    with open(filename, 'r') as f:
        wordlist = f.read().splitlines()
        for i in wordlist:
            if i[0:2] == 'at':
                output.append(('@' + i[2:] + ' : ' + i))
            elif i[0:1] == 'a':
                output.append('@' + i[1:] + ' : ' + i)
    output.sort(key = len)
    return '\n'.join([' '.join(output[0:10]), ' '.join(output[-10:])])

def main():
    if len(argv) > 1:
        print(find_handles(argv[1]))
    else:
        print(find_handles(raw_input('Enter a word file: ')))

if __name__ == '__main__':
    main()