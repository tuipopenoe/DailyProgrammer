#!python2
# Tui Popenoe
# challenge147E - Sports Points

import sys

def valid_score(score):
    invalid_scores = [1,2,4,5]
    if score not in invalid_scores:
        return True
    else:
        return False

def main():
    if len(sys.argv) > 1:
        print(valid_score(int(sys.argv[1])))
    else:
        print(valid_score(int(raw_input('Enter a score to validate: '))))

if __name__ == '__main__':
    main()