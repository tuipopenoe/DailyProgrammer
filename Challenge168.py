# Tui Popenoe
# Challenge #168

import sys

def generateGrades(n):
    output = n*[None]

    for i in range(n):
        output[i] = Student(firstName = generateFirstName(), \
                            lastName = generateLastName(), \
                            score1 = generateScore(), \
                            score2 = generateScore(), \
                            score3 = generateScore(), \
                            score4 = generateScore(), \
                            score5 = generateScore())

def generateLastName():

def generateFirstName():

def generateScore():

def main():
    generateGrades(sys.argv[1])

class Student(object):
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
            for key in kwargs:
                setattr(self, key, kwargs)

if __name__ == "__main__":
    main()