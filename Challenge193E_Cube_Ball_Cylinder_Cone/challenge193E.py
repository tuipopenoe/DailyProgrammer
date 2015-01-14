#!/usr/bin/env python
# Tui Popenoe
# challenge193E.py - Cube, Ball, Cylinder, Cone

import math
import sys

def describe_shapes(volume):
    cube = math.pow(volume, 1.0 / 3.0)
    sphere = math.pow((volume * 3.0) / (4.0 * math.pi), 1.0 / 2.0)
    cylinder = math.pow(volume / math.pi, 1.0 / 3.0)
    cone = math.pow(3 * volume / math.pi, 1.0 / 3.0)

    print('Cube: %sm wide, %s high, %sm tall' % (cube, cube, cube))
    print('Sphere: %sm tall, Diameter of %sm' % (sphere, sphere))
    print('Cylinder: %sm Radius' % cylinder)
    print('Cone: %sm tall, %sm Radius' % (cone, cone))

def main():
    if len(sys.argv) > 1:
        describe_shapes(float(sys.argv[1]))
    else:
        describe_shapes(float(sys.stdin.readline()))

if __name__ == '__main__':
    main()