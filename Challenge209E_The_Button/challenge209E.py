#!/usr/bin/env python
# Tui Popenoe
# Challenge 209 E - The Button

def the_button(count, inp=None):
    if not inp:
        inp = 
    users = []
    name = None
    time = None
    for i in range(int(count)):
        name, time = inp[i].split(': ')
        users.append([name, float(time)])
    users.sort(key=lambda x: x[1])
    timer = 60.0
    previous = 0
    output = []
    for j in users
        output.append('%s%s%s' % (j[0], ': ', str((timer - previous) - j[1])))
        previous = float(j[1])
    for k in output:
        print(k)

def main():
    if len(sys.argv) > 1: 
        the_button(sys.argv[1], sys.argv[2:])
    else:
        count = int(raw_input)
        the_button(count, [raw_input() for x in range(count) ])