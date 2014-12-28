#!python2
# Tui Popenoe
# challenge133E.py - Foot Traffic Analysis

import sys

def analyze():
    events = int(raw_input())
    rooms = {}
    for i in range(events):
        # Visitor ID, Room Index, In/Out, Timestamp
        line = raw_input().split()
        line[0] = int(line[0])
        line[1] = int(line[1])
        line[3] = int(line[3])
        if line[2] == 'I':
            # Increase time
            rooms.get(line[0], line[0])[0] += line[3]
            # Increase visitor count
            rooms.get(line[0], line[0])[1] += 1
        elif line[2] == 'O':
            # Decrease time
            rooms.get(line[0], line[0])[0] -= line[3]
        else:
            # Error
            print('Error')
            sys.exit()
    for key, value in rooms.iteritems():
        average = value[0] / value[1]
        print('Room %s, %s minute average visit, %s visitor(s) total' \
              % (key, average, value[1]))

def main():
    analyze()

if __name__ == '__main__':
    main()