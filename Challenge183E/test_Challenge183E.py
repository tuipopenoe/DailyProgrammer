#!python2
# Tui Popenoe
# Challenge183E.py -Semantic Version Sort

from Challenge183E import *

def test_semantic_version_sort(filename='test_input.txt'):
    test_values = ['20.1.1+i386', '2.0.12+i386', '2.0.11+i386', '2.0.11-alpha',
        '1.2.34', '0.20.7+20141005', '0.1.7+amd64']
    self.assertEqual(semantic_version_sort(filename), test_values)

def main():
    test_semantic_version_sort()

if __name__ == '__main__':
    main()