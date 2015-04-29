#!/usr/bin/env python
# Tui Popenoe
# challenge212e.py Rovarspraket
from sys import argv

def rovarspraket(string):
    output = []
    vowels_and_punc = {'a', 'e', 'i', 'o', 'u', 'y', '\'', '?', '"', '!', ',', '.', ' ', '*', '&', '%', '$', '#', '@', '(', ')'}
    for i in string:
        if i.lower() not in vowels_and_punc:
            output.append('%so%s' % (i, i.lower()))
        else:
            output.append(i)
    return ''.join(output)

def test_rovarspraket():
    test_input1 = "I'm speaking Robber's language!"
    print(rovarspraket(test_input1))

    test_output = "I'mom sospopeakokinongog Rorobobboberor'sos lolanongoguagoge!"
    print(test_output)
    assert rovarspraket(test_input1) == test_output

def main():
    test_rovarspraket()
    if len(argv) > 1:
        print(rovarspraket(argv[1:]))
    else:
        print(rovarspraket(raw_input()))

if __name__ == '__main__':
    main()