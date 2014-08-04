# Tui Popenoe
# Challenge95E.py - Reversing Text in a File

def reverseText(filename):
    output = list()
    f = open(filename, 'r')
    text = f.read.splitlines()
    for i in text:
        output.append(i[::-1])
    f.close()
    return output

def main():
    if len(sys.argv) > 1:
        reverseText()
    else:
        reverseText(raw_input())

if __name__=='__main__':
    main()