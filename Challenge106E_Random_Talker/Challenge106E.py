#!python2
# Tui Popenoe
# challenge106E.py - Random Talker Part 1

import sys

punctuation = ['.', ',', ':', ';', '!', '?', '(', ')', '[', ']', '{', '}']

def random_talker(text):
    count = {}
    for i in text:
        if i[-1] in punctuation:
            count[i[-1]] += 1
        if not i in count:
            count[i] = 1
        else:
            count[i] += 1
    return count

def top_ten(dct):
    items = sorted((v, k) for k, v in dct.iteritems()), reverse=True)
    return take(10, items.iteritems())

def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')
        l = f.read().split()
        words =random_talker(l)
        print(top_ten(words))
    else:
        l = raw_input().split()
        words = random_talker(l)
        print(top_ten(words))

if __name__ == '__main__':
    main()
