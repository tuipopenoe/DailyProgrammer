#!python2
# Tui Popenoe
# Challenge36E.py - 1000 Lockers

def one_thousand_lockers():
    lockers = [False] * 1000
    for i in range(1, 1000):
        for j in range(1, 1000):
            if i % j == 0:
                lockers[i] = not lockers[i]
    return (lockers.count(True), 
        [x for x in range(len(lockers)) if lockers[x] == True])

def main():
    print(one_thousand_lockers())

if __name__ == '__main__':
    main()