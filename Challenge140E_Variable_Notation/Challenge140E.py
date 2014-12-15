# Tui Popenoe
# Challenge140E.py - Variable Notation

def camelCase(text):
    output = ''.join(x.capitalize() for x in text.split())
    output[0].lower()
    #print(output)
    return output

def snakeCase(text):
    output = '_'.join(x.lower() for x in text.split())
    #print(output)
    return output

def screamingSnakeCase(text):
    output = '_'.join(x.upper() for x in text.split())
    #print(output)
    return output

def getInput():
    choice = raw_input()
    text = raw_input()
    return [choice, text]

def main():
    choice = getInput()
    text = choice[1]

    if choice[0] == '0':
        print(camelCase(text))

    if choice[0] == '1':
        print(snakeCase(text))

    if choice[0] == '2':
        print(screamingSnakeCase(text))

if __name__=='__main__':
    main()