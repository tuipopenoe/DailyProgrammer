# Tui Popenoe
# Challenge129E.py Longest Two-Character Sub-String

import sys

def twoCharacterSubString(input):
    currentLongest = input[:2]
    currentString = currentLongest

    if input[0] == input[1]:
        lastRun = input[:2]
    else:
        lastRun = input[1]

    for element in input[2:]:
        if element in lastRun:
            lastRun += element
        if element in currentString:
            currentString += element
        else:
            currentString = lastRun + element
            lastRun = element
        if len(currentString) >= len(currentLongest):
            currentLongest = currentString

    return currentLongest

def main():
    string = raw_input()
    print(twoCharacterSubString(string))

if __name__=='__main__':
    main()
