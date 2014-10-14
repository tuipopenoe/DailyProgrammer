#!python
# Tui Popenoe
# Challenge17E.py - Triangle 

def triangle(height):
    for i in range(height + 1):
        line = ['@'] * 2 ** i
        print(''.join(line))

def main():
    triangle(int(raw_input("Enter a triangle height: ")))

if __name__ == '__main__':
    main()