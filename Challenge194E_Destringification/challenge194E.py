#!python2
# Tui Popenoe
# challenge194E.py - Destringification

import sys

def destringify(string):
    """Return the unescaped string.
    Args: string-> The string to unescape
    Rets: the unescaped string
    """
    print(string.decode('string_escape'))


def main():
    if len(sys.argv) > 1:
        destringify(' '.join(sys.argv[1:]))
    else:
        destringify(raw_input('Enter string to destringify: '))

if __name__ == '__main__':
    main()
