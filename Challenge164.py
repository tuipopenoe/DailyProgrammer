# Tui Popenoe
# Challenge 164 Assemble this Scheme
""" 
    Implementation of basic programming problems in python. 
"""

def printHello():
    """Output 'Hello World' to the console."""
    print("Hello World")

def threeFive():
    """Output a list of the first 100 integers divisble by 3 and 5."""
    count = 0
    i = 0
    list = []
    while count < 100:
        if i % 3 == 0 and i % 5 == 0:
            list.append(i)
            count += 1
        i += 1
    return list

def isAnagram(word1, word2):
    """Return True if word1 is an anagram of word2."""
    if len(word1) == len(word2):
        if ''.join(sorted(word1)) == ''.join(sorted(word2)):
            return True

    return False

def removeLetter(letter, word):
    """Return a string where all instances of letter are removed."""
    truncated = ""

    for i in word:
        if word[i] == letter:
            pass
        else:
            truncated += i
    return truncated

def sumElements(array):
    """Return the sum of elements in an array."""
    return sum(array)