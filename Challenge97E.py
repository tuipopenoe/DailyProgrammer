# Tui Popenoe
# Challenge97E.py Concatenate Directory

import sys
import os

def concatDir():
    output = open('output.txt', 'a')
    for filename in os.listdir(sub_dir):
        with open(os.path.join(sub_dir, filename), 'r') as f:
            statinfo = os.stat(filename)
            s = f.read(filename)
            output.write('=== ' + filename + statinfo.st_size + '\n')
            output.write(s)
            output.write('\n')

    output.close()

def main():
    main()

if __name__=='__name__':
    main()