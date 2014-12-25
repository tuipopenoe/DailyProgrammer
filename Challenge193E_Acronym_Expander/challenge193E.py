#!python2
# Tui Popenoe
# challenge193E.py - Acronym Expander

import sys

acronyms = {'lol' : 'laugh out loud',
            'dw' : 'don\'t worry',
            'hf' : 'have fun',
            'gg' : 'good game',
            'brb' : 'be right back',
            'g2g' : 'got to go',
            'wtf' : 'what the fuck',
            'wp' : 'well played',
            'gl' : 'good luck',
            'imo' : 'in my opinion'
            }

def expand_acronyms(inp):
    """Expand all the acronyms in inp and return the full sentence.
    Args: inp -> The input string
    Rets: The expanded string.
    """
    inp = inp.split()
    output = []
    for i in inp:
        if i in acronyms:
            output.append(acronyms[i])
        else:
            output.append(i)
    return ' '.join(output)

def main():
    if len(sys.argv) > 1:
        print(expand_acronyms(' '.join(sys.argv[1:])))
    else:
        print(expand_acronyms(raw_input('Enter a string: ')))

if __name__ == '__main__':
    main()
