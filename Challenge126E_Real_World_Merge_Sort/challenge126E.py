#!python2
# Tui Popenoe
# challenge126E.py - Real World Merge Sort

import ast
import sys

def merge_sort(list_a):
    if len(list_a) > 1:
        # Floor division (integer division)
        mid = len(list_a) // 2
        left_half = list_a[:mid]
        right_half = list_a[mid:]
        # Recursively sort both halves of the list
        merge_sort(left_half)
        merge_sort(right_half)
        # Initialize count variables
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list_a[k] = left_half[i]
                i += 1
            else:
                list_a[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            list_a[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            list_a[k] = right_half[j]
            j += 1
            k += 1

def main():
    if len(sys.argv) > 1:
        list_a = ast.literal_eval(sys.argv[1])
        list_b = ast.literal_eval(sys.argv[2])
        list_b = list_b[len(list_a):]
        list_a.extend(list_b)
        merge_sort(list_a)
    else: 
        s = raw_input('Enter list A: ')
        list_a = map(int, s.split())
        s = raw_input('Enter list B: ')
        list_b = map(int, s.split())
        list_b = list_b[len(list_a):]
        list_a.extend(list_b)
        merge_sort(list_a)

    print(list_a)

if __name__ == '__main__':
    main()