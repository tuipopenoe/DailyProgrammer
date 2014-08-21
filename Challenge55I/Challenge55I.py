#!python2
# Tui Popenoe
# Challenge55I.py - Validating Input

from sys import argv

def display_sum(user_input):
    inp = user_input.split(' ')
    if int(inp[0]) >= 0 and int(inp[0]) <= 9:
        if int(inp[1]) >= 1 and int(inp[1]) <= 9:
            s = int(inp[0]) + int(inp[1])
            print(inp[0] + ' + ' + inp[1] + ' = ' + str(s))
            return
    print('Invalid')
    return

def main():
    if len(argv) > 1:
        display_sum(argv[1])
    else:
        display_sum(raw_input("Enter two integers 0 - 9 on one line: "))

if __name__ == '__main__':
    main()