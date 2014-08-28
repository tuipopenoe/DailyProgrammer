#!python2
# Tui Popenoe
# Challenge47I.py - Number Translate

from sys import argv

cipher = {
    'ze' : 0,
    'on' : 1,
    'tw' : 2,
    'th' : 3,
    'fo' : 4,
    'fi' : 5,
    'si' : 6,
    'se' : 7,
    'ei' : 8,
    'ni' : 9
}

def translate_number(num):
    output = list()
    #for i in num:
    output.append(cipher[num[:2]])
    return output

def main():
    if len(argv) > 1:
        print(translate_number(argv[1]))
    else:
        print(translate_number(raw_input("Enter an english number: ")))

if __name__ == '__main__':
    main()