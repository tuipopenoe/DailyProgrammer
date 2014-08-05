# Tui Popenoe
# Challenge139E.py - Pangrams

"""Returns true if the given string is a pangram, i.e. contains every letter 
    in the given language"""

def pangram(string=None, language=None):
    if string is None:
        print('Enter string: ')
        string = raw_input()

    if language is None:
        language = english = ['a','b','c','d','e','f','g','h','i','j','k','l',\
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in range(len(string)):
        for j in range(len(language)):
            if string[i].lower() == language[j]:
                language.pop(j)
                break

    # print('language: ')
    # print(language)
    # All the letters have been popped from the list
    if not language:
        print('True')
        return True
    else:
        print('False')
        return False

def main():
    pangram()

if __name__ == '__main__':
    main()