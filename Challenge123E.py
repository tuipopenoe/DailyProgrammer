# Tui Popenoe
# Challenge123E.py - Edge Sorting

import sys

def edgeSorting(lst):
    edges = list()
    for i in range(1, int(lst[0])):
        edges.append({
                'vert' : [lst[i][2], lst[i][4]],
                'vertName' : lst[i][0]
            })
    sorted_edges = sorted(edges, key=lambda k: k['vert'])

    for i in sorted_edges:
        print(i['vertName'] , i['vert'])
    return sorted_edges

def getInput(filename=None):
    if filename == None:
        n = raw_input()
        l = list()
        for i in range(int(n)):
            j = raw_input().split()
            for k in j:
                l.append(k)
    else:
        f = open(filename, 'r')
        l = f.readlines()

    l = map(lambda s: s.strip(), l)
    return l

def main():
    if len(sys.argv) > 1:
        return edgeSorting(getInput(sys.argv[1]))
    else:
        return edgeSorting(getInput())

if __name__=='__main__':
    main()

