#!/usr/bin/envy python
# Tui Popenoe
# Challenge215 E Sad Cycles

from math import pow
from sys  import argv

def sad_cycles(b, n):
    """Output the b sad-cycle for the number n."""
    output = []
    while len(output) == len(set(output)):
        if output == []:
            str_n = str(n)
        num = 0
        for i in str_n:
            num += int(pow(int(i), int(b)))
        if str(num) not in output:
            output.append(str(num))
            str_n = str(num)
        else:
            break
    return output


def test_sad_cycles():
    print(sad_cycles(2, 12))
    assert sad_cycles(2, 12) == ['5', '25', '29', '85', '89', '145', '42', '20', '4', '16', '37', '58']


def main():
    test_sad_cycles()
    if len(argv) > 1:
        print(sad_cycles(argv[1], argv[2]))
    else:
        print(sad_cycles(raw_input('Enter b: '),
                         raw_input('Enter n: ')))


if __name__ == '__main__':
    main()