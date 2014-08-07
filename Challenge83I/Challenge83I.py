# Tui Popenoe
# Challenge83I.py - Indexed File Search

import ast

def index_files(fileList):
    masterIndex = {}
    for i in fileList:
        f = open(i, 'r')
        words = f.read.split()

        for j in words:
            if j in masterIndex:
                masterIndex[j].append(i)
            else:
                masterIndex[j] = [i]
    return masterIndex

def index_words(fileList):
    index = list() 
    for i in fileList:
        f = open(i, 'r')
        words = f.read().split()
        wordIndex = {}
        for j in range(len(words)):
            if words[j] in wordIndex:
                wordIndex[words[j]].append(j)
            else:
                wordIndex[words[j]] = [j]


def search_words(wordList, index):
    output = list()
    for i in wordList:
        if i in index:
            output.append(index[i])
        else:
            pass
    # if the number of instances equals the length of the words searched,
    # then all the words exist in that file, and return it as a match
    found = [x for x in output if output.count(x) == len(wordList)]
    return found

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'index':
            files = index_files(sys.argv[2:])
            with open('index.txt', 'w') as f:
                f.write(files)
        if sys.argv[1] == 'search':
            with open('index.txt', 'r') as f:
                s = f.read()
                index = ast.literal_eval(s)
                files = search_words(sys.argv[2:], index)
                print(files)
    else:
        print('Invalid arguments')
        print('Use "index file1 file2 file3 ..."')
        print('Or "search word1 word2 word3..."')