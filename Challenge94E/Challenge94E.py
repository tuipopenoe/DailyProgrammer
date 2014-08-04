# Tui Popenoe
# Challenge94E.py - Elemental Symbols in Strings

import sys

elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 
    'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 
    'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 
    'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
    'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt',
    'Au', 'Hg', 'Ti', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Rf', 'Db', 
    'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Uut', 'Fl', 'Uup', 'Lv', 'Uus',
    'Uuo', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 
    'Er', 'Tm', 'Yb', 'Lu', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 
    'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']

def breakBad(string):
    output = list()
    for i in range(len(string)-1):
        for j in elements:
            if string[i].upper() == j:
                output.append(string[:i] + '[' + j + ']' + string[i+1:])
            elif (string[i].upper() + string[i+1]) == j:
                output.append(string[:i] + '[' + j + ']' + string[i+2:])
    return output

def main():
    if len(sys.argv) > 1:
        for i in breakBad(sys.argv[1]):
            print(i)
    else:
        for i in breakBad(raw_input()):
            print(i)

if __name__=='__main__':
    main()