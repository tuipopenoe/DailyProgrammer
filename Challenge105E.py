# Tui Popenoe
# Challenge105E.py Word Unscrambler

import sys

def unscrambleWords(scrambledWords, wordList):
    output = list()
    for i in scrambledWords:
        for k in wordList:
            if len(i) > len(k):
                if anagram(i, k):
                    output.append(k)
            else:
                if(anagram(k, i)):
                    output.append(k)

    print(output)
    return output


def anagram(word1, word2):
    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i] == word2[j]:
                word1.pop(i)

    if len(word1) == 0:
        return True
    else:
        return False

def main():
    if len(sys.argv) > 1:
        unscrambleWords(sys.argv[1], sys.argv[2])
    else:
        pass

if __name__=='__main__':
    main()