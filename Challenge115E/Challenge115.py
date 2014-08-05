# Tui Popenoe
# Challenge115.py - Word Ladder

import sys

def buildGraph(filename):
    d = {}
    f = open(filename, 'r')
    for line in f:
        if line[-1] == '\n':
            word = line[:-1]
        else:
            word = line
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = word
    f.close()
    for key, value in d.iteritems():
        print(key, value)
    return d

def main():
    if len(sys.argv) > 1:
        buildGraph(sys.argv[1])
    else:
        buildGraph(raw_input())

if __name__=='__main__':
    main()