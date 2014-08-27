#!python2
# Tui Popenoe
# Challenge40E.py - Print 1 to 1000 with no conditionals or loops.

# apply function str() to every item in iterable and return list of results
# use '\n'.join to convert list to series of lines
print '\n'.join(map(str, range(1,1001)))