# Tui Popenoe
# Challenge 154 - March Madness Brackets

def removeBrackets(string):
    brackets = ['[', ']', '{', '}', '(', ')']
    for i in brackets: 
        string = string.replace(i, '')

    print string
