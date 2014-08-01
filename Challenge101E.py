# Tui Popenoe
# Challenge101E.py - Non Repeating Years

import sys

def non_repeating_years(n, m):
    non_repeating = list()
    count = 0
    digits = list()
    for i in range(int(n, m)):
        s = str(i)
        for j in s:
            if j not in s:
                digits.append(s)
        if len(digits) == 4:
            count += 1
            non_repeating.append(''.join(digits))
        else:
            count = 0
        del digits[:]

    return (non_repeating, count)

def main():
    if len(sys.argv) > 1:
        print(non_repeating_years(sys.argv[1], sys.argv[2]))
    else:
        print(non_repeating_years(raw_input(), raw_input()))

if __name__=='__main__':
    main()