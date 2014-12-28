#!python2
# Tui Popenoe
# challenge133E.py - Foot Traffic Analysis

import sys

def analyze():
    events = int(raw_input())
    rooms = {}
    for i in range(events):
        # Visitor ID, Room Index, In/Out, Timestamp
        data = raw_input().split()
        # Initialize key value pair if doesn't exist
        if data[1] not in rooms:
            rooms[data[1]] = [0, 0]
        # If the In/Out flag is 'I'
        if data[2].upper() == 'I':
            # Increase time value[0]
            rooms[data[1]][0] -= int(data[3])
            # Increase visitor count value[1]
            rooms[data[1]][1] += 1
        elif data[2].upper() == 'O':
            # Decrease time
            rooms[data[1]][0] += int(data[3])
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