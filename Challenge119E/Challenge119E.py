# Tui Popenoe
# Challenge119E.py - Change Calculator

"""Takes an ammount of money and returns the minimum number of coins needed to 
equal that amount of money."""

import sys

def changeCalculator(n):
    #Convert dollar input to coin input
    n = int(float(n) * 100)
    coins = minCoins(n)
    print("Quarters", coins[0])
    print("Dimes", coins[1])
    print("Nickels", coins[2])
    print("Pennies", coins[3])


def minCoins(n):
    # List storing change in [Quarters, Dimes, Nickels, Pennies]
    change = [0, 0, 0, 0]
    if n / 25 > 0:
        change[0] = n / 25
        n = n % 25
    if n / 10 > 0:
        change[1] = n / 10
        n = n % 10
    if n / 5 > 0:
        change[2] = n / 5
        n = n % 5
    if n / 1 > 0:
        change[3] = n / 1
        n = n % 1

    return change

def main():
    if len(sys.argv) > 1:
        changeCalculator(float(sys.argv[1]))
    else:
        print("Enter an amount of money to be converted: ")
        changeCalculator(int(raw_input()))

if __name__ == "__main__":
    main()