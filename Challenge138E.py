# Tui Popenoe
# Challenge138E.py Repulsion Force
"""Calculate the repulsion force between two particles of given mass and 
    location"""

import math

def repulsionForce(mass1=None, x1=None, y1=None, mass2=None, x2=None, y2=None):
    force = ((mass1 * mass2) / math.pow(distance(x1,x2,y1,y2), 2))
    print(force)
    return force

def distance(x1, x2, y1, y2):
    deltaX = (x1 - x2)
    deltaY = (y1 - y2)

    return math.sqrt(deltaX*deltaX + deltaY*deltaY)

def main():
    print('Enter <mass> <position x> <position y> for particle 1: ')
    args = raw_input().split()
    print('Enter <mass> <position x> <position y> for particle 2: ')
    args2 = raw_input().split()

    for i in range(len(args)):
        args[i] = float(args[i])

    repulsionForce(args[0], args[1], args[2], args2[0], args2[1], args2[2])

if __name__=='__main__':
    main()