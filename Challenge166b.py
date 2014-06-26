# Tui Popenoe
# Challenge 166b Planetary Gravity

import sys
import math

def calcVolume(r):
    return (4/3) * (math.pi * pow(r, 3))

def calcMass(v, d):
    return v*d

def calcForce(m1, m2, d):
    g = (m1 * m2) / pow(d, 2)

def calcWeight(planets):
    f = open("input.txt", 'r')

    mass = int(f.readline())
    planets = int(f.readline())
    weight = []

    for i in range(planets):
        p = f.readline().split(',')

        m2 = calcMass(calcVolume(p[1]), p[2])
        force = calcForce(mass, m2, p[1])
        weight.append(force)

    return weight

def main():
    calcWeight()

if __name__=='__main__':
    main()