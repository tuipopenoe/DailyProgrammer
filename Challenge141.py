# Tui Popenoe
# Challenge 141 Checksums

"""Create the Fletcher's 16-bit checksum for the given lines of text input."""

def createChecksum(text):
    sum1 = 0
    sum2 = 0
    for elem in (ord(x) for x in text):
        sum1 = (sum1 + elem) % 255
        sum2 = (sum2 + sum1) % 255

    return str(hex((sum2 << 8) | sum1)).replace('0x', '').upper()

def printOutput(text):
    for i in text:
        print(i)

def main():
    n = raw_input()
    output = list()
    for i in range(int(n)):
        text = raw_input()
        output.append([i+1, createChecksum(text)])
    printOutput(output)

if __name__=='__main__':
    main()