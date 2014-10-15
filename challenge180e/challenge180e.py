#!python2
# Tui Popenoe
# challenge180e.py - Look'n'Say

def look_n_say(n=6):
    """Prints successive strings where the current string is the previous
    string as if read aloud."""
    output = []
    output.append([1])
    print(output)
    for i in range(n):
        print('i: ', i)
        dct = {}
        lst = []
        for j in range(len(output[i])):
            if dct.get(output[i][j]):
                dct[output[i][j]] += 1
            else:
                dct[output[i][j]] = 1
        for key, value in dct.iteritems():
            lst.append(value)
            lst.append(key)
        output.append(lst)
        print(lst)
        print(output)
        del lst[:]

def main():
    look_n_say()

if __name__ == '__main__':
    main()