# Tui Popenoe
# Challenge 168 (E) String Index

import re
import sys
import unittest

class StringIndex():
    """
    StringIndex class containing methods for searching word indices in a string
    """

    def indexString(self, string):
        """ (str) -> list
        Returns a list of the words in a string
        """
        lst = ['']
        lst = re.findall(r"[a-zA-Z0-9]+", string)
        for i in lst:
            print(i)
        return lst


    def getWordAt(self, i, lst):
        """ (int, list)
        Returns the item at index i in the list
        """
        return lst[i]

    def getWords(self, lst, indices=None):
        """ (list) -> list
        Return a list of words for the given indices
        """
        words = list()
        if indices is not None:
            pass
        else:
            indices = raw_input().split()
        for i in indices:
            words.append(self.getWordAt(int(i), lst))
        return words

    def main(self):
        """ None -> None
        Print a string containing the indices of words in an input string
        """
        self.words = self.indexString(sys.argv[1])
        print(self.getWords(self.words))

class TestStringIndex(unittest.TestCase):


if __name__=='__main__':
    main()

