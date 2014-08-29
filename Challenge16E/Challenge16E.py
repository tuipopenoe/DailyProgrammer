#!python2
# Tui Popenoe
# Challenge16E.py - Remove First Instance

from ast import literal_eval

def remove_first_instance(lst, remove):
    lst = list(lst)
    for i in lst:
        if i in remove:
            lst.remove(i)
            return ''.join(lst)

def main():
    print(remove_first_instance(raw_input("Enter string: "),
        raw_input("Remove any of : ")))

if __name__ == '__main__':
    main()
