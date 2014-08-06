# Tui Popenoe
# Challenge86E.py - Run Length Encoding

import sys

def run_length_encoding(string):
    runs = {}
    output = list()
    for i in string:
        if i in runs:
            runs[i] += 1
        else:
            runs[i] = 1

    for key, value in runs.iteritems():
        output.append(key)
        output.append(str(value))

    print ''.join(output)

def main():
    if len(sys.argv) > 1:
        run_length_encoding(sys.argv[1])
    else:
        run_length_encoding(raw_input())

if __name__=='__main__':
    main()