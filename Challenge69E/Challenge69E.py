# Tui Popenoe
# Challenge69E.py - List Input

import ast

def get_list(filename):
    with open(filename, 'r') as f:
        lst = f.readline()
        title = lst.split("'")[1]
        rest = f.read()[5:] # [len(lst)+5:]
        data = ast.literal_eval(rest)

    print(title)
    for i in data:
        print(i)

def main():
    get_list(sys.argv[1])

if __name__ == '__main__':
    main()


