# Tui Popenoe
# Challenge125E.py - Word Analytics

import sys
import re

def wordAnalytics(filename):
    f = open(filename, 'r')
    l = f.read()
    words = l.split()
    letters = list()
    symbols = list()

    for i in words:
        for j in i:
            letters.append(j)

    for i in letters:
        if not re.match('[a-zA-Z_0-9]', i):
            symbols.append(i)
            letters.remove(i)

    print(len(words))
    print(len(letters))
    print(len(symbols))
    topThree(words)
    topThree(letters)

def mostCommon(lst):
    return max(set(lst), key=lst.count)

def removeCommon(lst, char):
    for i in lst:
        if i == char:
            lst.remove(i)

def topThree(lst):
    common = mostCommon(lst)
    for i in range(3):
        print(common)
        lst = removeCommon(lst, common)

def main():
    if len(sys.argv) > 1:
        wordAnalytics(sys.argv[1])
    else:
        wordAnalytics(raw_input)

if __name__=='__main__':
    main()