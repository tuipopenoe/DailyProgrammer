# Tui Popenoe
# Challenge68E.py - Emirp

import sys


def primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in xrange(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]


def emirp(n):
    """ Return a list of the emirp < n """
    output = list()
    set_primes = primes(n*10)
    prime_numbers = primes(n)
    #print(prime_numbers)
    for i in prime_numbers:
        if int(str(i)[::-1]) in set_primes and str(i) != str(i)[::-1]:
            output.append(i)
    return output


def main():
    if len(sys.argv) == 2:
        print(emirp(int(sys.argv[1])))
    else:
        print(emirp(int(raw_input())))


if __name__ == '__main__':
    main()
