#!/usr/bin/env python
# Tui Popenoe
# challenge198E.py - Words With Enemies

import sys

def battle_words(word1, word2):
    winner = bust_words(word1, word2)
    if len(winner[0]) > len(winner[1]):
        return 'Left: %s' % ''.join(winner)
    elif len(winner[1]) > len(winner[0]):
        return 'Right: %s' % ''.join(winner)
    else:
        return 'Tie: %s' % ''.join(winner)

def bust_words(word1, word2):
    if len(word1) > len(word2):
        for i in word1:
            if i in word2:
                word1 = word1.replace(i, '')
                word2 = word2.replace(i, '')
    else:
        for i in word2:
            if i in word1:
                word1 = word1.replace(i, '')
                word2 = word2.replace(i, '')
    return [word1, word2]

def main():
    if len(sys.argv) > 1:
        print(battle_words(sys.argv[1], sys.argv[2]))
    else:
        words = sys.stdin.readline().split()
        print(battle_words(words[0], words[1]))

if __name__ == '__main__':
    main()