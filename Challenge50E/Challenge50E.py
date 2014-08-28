#!python2
# Tui Popenoe
# Challenge50E.py - Store Credit

from ast import literal_eval

def max_store_credit(credit, lst):
    lst.sort(reverse=True)
    max_item_location = None
    max_pair_value = 0
    max_pair = []
    print(lst)
    for i in  range(len(lst)):
        if lst[i] < credit:
            max_item_location = i
            max_item = lst[i]
            break
    for i in range(max_item_location, len(lst)):
        for j in range(i+1, len(lst)):
            print(lst[i], lst[j])
            if lst[i] + lst[j] > max_pair_value and lst[i] + lst[j] <= credit:
                max_pair = [lst[i], lst[j]]
                max_pair_value = lst[i] + lst[j]
    return max_pair

def exact_store_credit(credit, lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == credit:
                return (i, j)
    return None

def main():
    with open('input.txt', 'r') as f:
        credit = int(f.readline())
        lst = literal_eval(f.read())
        print(exact_store_credit(credit, lst))

if __name__ == '__main__':
    main()
