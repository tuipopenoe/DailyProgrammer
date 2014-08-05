# Tui Popenoe
# Challenge98E.py - Arithmetic Tables

import sys

def arithmeticTables(symbol, number):
    line = symbol + ' | '
    for i in range(number + 1):
        line += str(i) 
    print(line)
    for i in range(number + 2):
        if i == 0:
            line += str(i)
        elif i == 1:
            line += ' | '
        for j in range(number+1):
            line += str(number + number)
        print(line)

def main():
    arithmeticTables('*', sys.argv[1])

if __name__=='__main__':
    main()