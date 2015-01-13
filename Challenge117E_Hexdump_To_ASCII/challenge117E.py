#!python2
# Tui Popenoe
# challenge117E.py - Hexdump to ASCII

def hexdump(filename):
    try:
        output = []
        with open(filename, 'rb') as f:
            byte = f.read(1)
            while byte != '':
                output.append(format(byte, '02x'))
                byte = f.read(1)
        return output
    except Exception, ex:
        print(ex)

def main():
    if len(sys.argv) > 1:
        hexdump(sys.argv[1])
    else:
        hexdump(sys.stdin.readline())

if __name__ == '__main__':
    main()