#!/usr/bin/env python
# Tui Popenoe
# Challenge220E.py Mangling Sentences

from sys import argv

def mangle_sentence(sentence):
    """Return the given sentence sorted in letter order."""
    if isinstance(sentence, basestring):
        lst = sentence.split(' ')
    elif isinstance(sentence, list):
        lst = setence
    output = []
    for i in lst:
        output.append(''.join(sorted(i)))
    return ' '.join(output)


def test_mangle_sentence(sentence):
    """Test the mangle_sentence() function."""
    assert mangle_sentence('hello') == 'ehllo'

def main():
    if len(arv) > 1:
        print(mangle_sentence(argv))
    else:
        (mangle_setence(raw_input('Enter a sentence to mangle: '))

if __name__ == '__main__':
    main()