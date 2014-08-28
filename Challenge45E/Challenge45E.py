#!python2
# Tui Popenoe
# Challenge45E.py - Checkerboard

from sys import argv

def print_border(num_squares, square_width):
    border = ['*'] * (num_squares * square_width)
    print(''.join(border))

def print_squares(num_squares, square_width, square_height, odd=False):
    line = list()
    odd_line = list()
    for j in range(num_squares / 2):
            line.extend([' '] * square_width)
            line.extend(['#'] * square_width)
            odd_line.extend(['#'] * square_width)
            odd_line.extend([' '] * square_width)
    for i in range(square_height):
        if not odd:
            print(''.join(line))
        else:
            print(''.join(odd_line))

def print_board(num_squares, square_width, square_height, board_height):
    print_border(num_squares, square_width)
    for i in range(board_height):
        if i % 2 == 0:
            print_squares(num_squares, square_width, square_height)
        else:
            print_squares(num_squares, square_width, square_height, True)
        print_border(num_squares, square_width)

def main():
    if len(argv) > 1:
        print_board(int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4]))
    else:
        pass

if __name__ == '__main__':
    main()