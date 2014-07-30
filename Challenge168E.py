# Tui Popenoe
# Challenge 168 (E) String Index

import argparse
import re
import sys
import unittest

class StringIndex():
    """
    StringIndex class containing methods for searching word indices in a string
    """
    def index_string(self, string):
        """ (str) -> list
        Returns a list of the words in a string
        """
        lst = ['']
        lst.extend(re.findall(r"\w+", string))
        print(lst)
        return lst


    def get_word_at(self, i, lst):
        """ (int, list)
        Returns the item at index i in the list
        """
        if i >= len(lst) or i < 0:
            return lst[0]
        else:
            return lst[i]

    def get_words(self, lst, indices=None):
        """ (list) -> list
        Return a list of words for the given indices
        """
        words = list()
        if indices is not None:
            pass
        else:
            indices = raw_input().split()
        for i in indices:
            words.append(self.get_word_at(int(i), lst))
        return words

    def main(self):
        """ None -> None
        Print a string containing the indices of words in an input string
        """
        self.words = self.index_string(sys.argv[1])
        print(self.get_words(self.words))

class TestStringIndex(unittest.TestCase):
    """
    Test class for testing StringIndex
    """
    def setUp(self):
        """
        Setup variables for the unit tests
        """
        self.testInput = '...You...!!!@!3124131212 Hello have this is a --- '\
            'string Solved !!...? to test @\n\n\n#!#@#@%$**#$@ Congratz'\
            ' this!!!!!!!!!!!!!!!!one ---Problem\n\n'
        self.testIndices = [12, -1, 1, -100, 4, 1000, 9, -1000, 16, 13, 17, 15]
        self.stringIndex = StringIndex()

    def test_index_string(self):
        """
        Test StringIndex index_string method
        """
        words = ['', 'You', '3124131212', 'Hello', 'have', 'this', 'is', 'a', \
            'string', 'Solved', 'to', 'test', 'Congratz', 'this', 'one', \
            'Problem']
        self.assertEqual(words, self.stringIndex.index_string(self.testInput))

    def test_get_word_at(self):
        """
        Test StringIndex get_word_at method
        """
        words = ['', 'All', 'your', 'base', 'are', 'belong', 'to', 'us']
        for i in range(len(words)):
            self.assertEqual(words[i], 
                self.stringIndex.get_word_at(int(i), words))
        self.assertEqual(words[0], 
            self.stringIndex.get_word_at(1000, words))

    def test_get_words(self):
        """
        Test StringIndex get_words method
        """
        words = ['Congratz', '', 'You', '', 'have', '', 'Solved', \
            '', '', 'this', '', 'Problem']
        print('Words: ')
        print(self.stringIndex.get_words(self.testInput,
            self.testIndices))
        self.assertEqual(words, self.stringIndex.get_words(
            self.stringIndex.index_string(self.testInput),
            self.testIndices))

if __name__=='__main__':
    if len(sys.argv) == 1:
        unittest.main()
    else:
        StringIndex.main()
