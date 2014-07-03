# Tui Popenoe
# Challenge 158 - The Torn Number

""" Verifies if an input number, when split into two separate numbers by taking the first half of the digits, adding them to the second half of the digits and squaring the result is equal to the original number."""

def tornNumber(n):
    num1 = n[:len(n)/2]
    num2 = n[len(n)/2:]

    print(num1)
    print(num2)

    # torn = (num1+num2) ** (num1+num2)

    # if torn == int(n):
    #     return True
    # else:
    #     return False

def main():
    tornNumbers = list()
    for i in range(10000):
        torn = str(i)
        if tornNumber(torn):
            tornNumbers.append(torn)

    print(tornNumbers)

if __name__=='__main__':
    main()