# Tui Popenoe
# Challenge80E.py - Anagrams

""" Given a line separated lowercase dictionary file, find anagrams for the
given input word. """

import sys


def find_anagrams(word, dictionary_file):
    output = list()
    with open(dictionary_file, 'r') as f:
        count = 0
        dictionary = f.read().splitlines()
        for element in dictionary:
            if len(word) == len(element):
                for i in word:
                    if i in element:
                        count += 1
                if len(word) == count:
                    output.append(element)
                else:
                    pass
                count = 0
            else:
                pass
    return output


def main():
    if len(sys.argv) == 2:
        print('\n'.join(find_anagrams(sys.argv[1], 'english_dictionary.txt')))
    elif len(sys.argv) == 3:
        print('\n'.join(find_anagrams(sys.argv[1], sys.argv[2])))
    else:
        print('Invalid arguments: search for a word in an english dictionary'
              'by default, or a word in a dictionary file')
        print('word')
        print('word dictionary_file')

if __name__ == '__main__':
    main()
