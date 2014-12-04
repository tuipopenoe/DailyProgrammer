#!python2
# Tui Popenoe
# challenge105E.py Word Unscrambler

import sys

def unscramble_words(scrambled_words, word_list):
    """Unscramble the words in a wordfile passed in and match wordlist"""
    output = []
    for i in scrambled_words:
        for k in word_list:
            if len(i) > len(k):
                if anagram(i, k):
                    output.append(k)
            else:
                if(anagram(k, i)):
                    output.append(k)
    print(output)
    return output


def anagram(word1, word2):
    for i, item1 in enumerate(word1):
        for j, item2 in enumerate(word2):
            if item1 == item2:
                word1.pop(i)
    if not word1:
        return True
    else:
        return False

def main():
    if len(sys.argv) > 1:
        unscramble_words(sys.argv[1], sys.argv[2])
    else:
        unscramble_words(raw_input('Enter a file: '),
                         raw_input('Enter a wordlist: '))

if __name__=='__main__':
    main()