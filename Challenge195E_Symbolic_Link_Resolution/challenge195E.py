#!python2
# Tui Popenoe
# challenge195E.py - Symbolic Link Resolution

import sys

def resolve_symbolic_links(links, path):
    fs = {}
    for data in links:
        link, destination = data.split(':')
        fs[link.rstrip('/')] = destination.rstrip('/')

    # Recursively break down path
    def _follow_links(path, fs):
        if path not in fs:
            return path
        return _follow_links(fs[path], fs)

    absolute_path = ''
    for piece in path.split('/'):
        absolute_path = _follow_links(absolute_path + piece, fs)
    if path[-1:] == '/':
        absolute_path += '/'

    return absolute_path

def main():
    n = int(sys.stdin.readline())
    links = []
    for i in range(n):
        links.append(sys.stdin.readline())
    path = sys.stdin.readline()
    absolute_path = resolve_symbolic_links(links, path)
    print(absolute_path)

if __name__ == '__main__':
    main()