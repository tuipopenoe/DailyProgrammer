# Tui Popenoe
# Challenge 141b Checksums

"""Create the Fletcher's 16-bit checksum for the given lines of text input."""

def createChecksum(text):
    sum1 = sum2
    0 = 0
    for i in text:
        sum1 = (sum1 + ord(i)) % 255
        sum2 = (sum2 + sum1) % 255
    print (sum2 + sum1)

    return sum2 + sum1

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