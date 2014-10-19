#!python2
# Tui Popenoe
# challenge176e.py - Pivot Table

def pivot_table(datafile='input.txt'):
    """Create a pivot table from the datafile."""
    data = []
    with open(datafile, 'r') as f:
        data = f.readlines()
        for i in data:
            i = i.split()
    week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    sums = []
    for j in week:
        sums.append(sum(d[2] for d in data if d[1] == j))
    sums = map(str, sums)
    print('    '.join(week))
    print('    '.join(sums))

def main():
    pivot_table()

if __name__ == '__main__':
    main()