# Tui Popenoe
# Challenge 164 Assemble this Scheme

def printHello():
    print("Hello World")

def threeFive():
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
    if len(word1) == len(word2):
        if ''.join(sorted(word1)) == ''.join(sorted(word2)):
            return True

    return False

def removeLetter(letter, word):
    truncated = ""

    for i in word:
        if word[i] == letter:
            pass
        else:
            truncated += i
    return truncated

def sumElements(array):
    return sum(array)