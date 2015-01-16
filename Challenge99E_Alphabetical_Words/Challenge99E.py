# Tui Popenoe
# Challenge99E.py

import sys

def alphabetical_order(word):
    for i in range(len(word)-1):
        if word[i+1] < word[i]:
            return False
    return True

def main():
    f = open(sys.argv[1], 'r')
    words = f.read().splitlines()
    ordered_words = list()
    f.close()
    count = 0
    for i in words:
        if alphabetical_order(i):
            count += 1
            ordered_words.append(i)

    print(count, ordered_words)

if __name__=='__main__':
    main()
