#!python2
# Tui Popenoe
# Challenge182E.py - The Column Co

from sys import argv

def column_conundrum(cols, col_width, space_width, text):
    line_width = cols * col_width + (cols - 1) * cols
    lines = [text[line_width:i+n] for i in range(0, line_width), n]



def main():
    column_conundrum(int(argv[0]), int(argv[1]), int(argv[2]), str(argv[3:]))

if __name__ == '__main__':
    main()