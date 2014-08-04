# Tui Popenoe
# Challenge106E.py - Random Talker Part 1

import sys

punctuation = ['.', ',', ':', ';', '!', '?', '(', ')', '[', ']', '{', '}']

def randomTalker(text):
    count = {}
    for i in text:
        if i[-1] in punctuation:
            count[i[-1]] += 1
        if not i in count:
            count[i] = 1
        else:
            count[i] += 1
    return count

def topTen(dct):
    items = sorted((v, k) for k, v in dct.iteritems()), reverse=True)
    return take(10, items.iteritems())


def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')
        l = f.read().split()
        words =randomTalker(l)
        print(topTen(words))
    else:
        l = raw_input().split()
        words = randomTalker(l)
        print(topTen(words))