# Tui Popenoe
# Challenge127E.py - McCarthy 91 Function

import sys

def mcCarthy91(n):
    if n == 91:
        return n
    if n > 100:
        print("M("+str(n)+")\t\tsince " + str(n) + " > 100")
        return mcCarthy91(n-10)
    if n <= 100:
        print("M(M("+str(n+11)+"))\tsince " + str(n) + "<= 100")
        return mcCarthy91(mcCarthy91(n+11))

def main():
    print("M("+sys.argv[1]+")) = ")
    if len(sys.argv) > 1:
        print(mcCarthy91(int(sys.argv[1])))
    else:
        print(mcCarthy91(int(raw_input)))

if __name__=='__main__':
    main()