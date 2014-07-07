# Tui Popenoe
# Challenge 141 Checksums

"""Create the Fletcher's 16-bit checksum for the given lines of text input."""

def createChecksum(text):
    """ Calculate the Fletcher's checksum of the given string."""
    sum1 = 0
    sum2 = 0

    # Given a string of length 1, use ord() to return the integer value of the
    # Unicode character. Loop through <text> one character at a time 
    for elem in (ord(x) for x in text):
        sum1 = (sum1 + elem) % 255
        sum2 = (sum2 + sum1) % 255

    # use hex() to convert integer of any size to hexadecimal prefixed by Ox
    # sum2 << 8 returns sum2 shifted left 8 places. Equivalent to sum2 * 2^8
    # | sum1 performs a bitwise or against sum2. Each bit of output is 0 if 
    # bit of sum1 and sum2 is 0. 
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