#!python2
# Tui Popenoe
# Challenge46E.py - Bit String Population

def get_population(str):
    bits = ''.join(format(ord(x), 'b') for x in str)
    print(bits)
    return len(bits)

def main():
    print(get_population(raw_input("Enter a string to get the population: ")))

if __name__ == '__main__':
    main()
