# Tui Popenoe
# Challenge174E.py - Thue-Morse Sequences 

def thue_morse():
    val = '01'
    for i in range(1, 7):
        val = str(twos_comp(int(val, 2), len(val)))
        print(val)

def twos_comp(val, bits):
    """Compute the 2's complement of int value val."""
    x = int(val, bits)
    num_bits = 10
    return x - (1 << num_bits)

def main():
    print(0)
    thue_morse()

if __name__=='__main__':
    main()