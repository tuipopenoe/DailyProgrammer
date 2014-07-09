# Tui Popenoe
# Challenge136E - Student Management

def studentManagement():
    studentsGrades = raw_input().split()

    # List comprehension grabbing input
    l = [raw_input().split() for i in range(int(studentsGrades[0]))]

    averages = [0] * studentsGrades[0]

    for i in l:
        for j in range(1, len(i)):
            averages[]
    print(l)


def main():
    studentManagement()

if __name__=='__main__':
    main()