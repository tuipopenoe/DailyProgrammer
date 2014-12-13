#!python2
# Tui Popenoe
# Challenge183E.py - Semantic Version Sort

def semantic_version_sort(filename='versions.txt'):
    with open(filename, 'r') as f:
        n = int(f.readline())
        versions = f.readlines()
        versions.sort()
        return versions

def main():
    semantic_version_sort()

if __name__ == '__main__':
    main()
