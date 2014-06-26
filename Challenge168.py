# Tui Popenoe
# Challenge #168 Final Grades

import sys
import random

def generateGrades(n, f, l):
    n = int(n)

    output = []

    for i in range(n):
        output.append({ 
                        'firstName' : generateFirstName(f), \
                        'lastName' : generateLastName(l), \
                        'score1' : generateScore(), \
                        'score2' : generateScore(), \
                        'score3' : generateScore(), \
                        'score4' : generateScore(), \
                        'score5' : generateScore()
                    })

    f = open('finalGrades.txt', 'w')

    for i in output:
        f.write(i['firstName'] +' ')
        f.write(i['lastName'] + ', \n')
        f.write(str(i['score1']) + ', ')
        f.write(str(i['score2']) + ', ')
        f.write(str(i['score3']) + ', ')
        f.write(str(i['score4']) + ', ')
        f.write(str(i['score5']) + '\n')

    f.close()

    return output

def generateLastName(lastNames):
    return lastNames[random.randint(0, len(lastNames)-1)]

def generateFirstName(firstNames):
    return firstNames[random.randint(0, len(firstNames)-1)]

def generateScore():
    return format(random.random()*100, '.2f')

def main(f, l):
    random.seed()
    generateGrades(sys.argv[1], f, l)




firstNames = \
[
'Aiden',
'Jackson',
'Ethan',
'Liam',
'Mason',
'Noah',
'Lucas',
'Jacob',
'Jayden',
'Jack',
'Logan',
'Ryan',
'Caleb',
'Benjamin',
'William',
'Michael',
'Alexander',
'Elijah',
'Matthew',
'Dylan',
'James',
'Owen',
'Connor',
'Brayden',
'Carter',
'Landon',
'Joshua',
'Luke',
'Daniel',
'Gabriel',
'Nicholas',
'Nathan',
'Oliver',
'Henry',
'Andrew',
'Gavin',
'Cameron',
'Eli',
'Max',
'Isaac',
'Evan',
'Samuel',
'Grayson',
'Tyler',
'Zachary',
'Wyatt',
'Joseph',
'Charlie',
'Hunter',
'David',
'Anthony',
'Christian',
'Colton',
'Thomas',
'Dominic',
'Austin',
'John',
'Sebastian',
'Cooper',
'Levi',
'Parker',
'Isaiah',
'Chase',
'Blake',
'Aaron',
'Alex',
'Adam',
'Tristan',
'Julian',
'Jonathan',
'Christopher',
'Jace',
'Nolan',
'Miles',
'Jordan',
'Carson',
'Colin',
'Ian',
'Riley',
'Xavier',
'Hudson',
'Adrian',
'Cole',
'Brody',
'Leo',
'Jake',
'Bentley',
'Sean',
'Jeremiah',
'Asher',
'Nathaniel',
'Micah',
'Jason',
'Ryder',
'Declan',
'Hayden',
'Brandon',
'Easton',
'Lincoln',
'Harrison',
'Sophia',
'Emma',
'Olivia',
'Isabella',
'Ava',
'Lily',
'Zoe',
'Chloe',
'Mia',
'Madison',
'Emily',
'Ella',
'Madelyn',
'Abigail',
'Aubrey',
'Addison',
'Avery',
'Layla',
'Hailey',
'Amelia',
'Hannah',
'Charlotte',
'Kaitlyn',
'Harper',
'Kaylee',
'Sophie',
'Mackenzie',
'Peyton',
'Riley',
'Grace',
'Brooklyn',
'Sarah',
'Aaliyah',
'Anna',
'Arianna',
'Ellie',
'Natalie',
'Isabelle',
'Lillian',
'Evelyn',
'Elizabeth',
'Lyla',
'Lucy',
'Claire',
'Makayla',
'Kylie',
'Audrey',
'Maya',
'Leah',
'Gabriella',
'Annabelle',
'Savannah',
'Nora',
'Reagan',
'Scarlett',
'Samantha',
'Alyssa',
'Allison',
'Elena',
'Stella',
'Alexis',
'Victoria',
'Aria',
'Molly',
'Maria',
'Bailey',
'Sydney',
'Bella',
'Mila',
'Taylor',
'Kayla',
'Eva',
'Jasmine',
'Gianna',
'Alexandra',
'Julia',
'Eliana',
'Kennedy',
'Brianna',
'Ruby',
'Lauren',
'Alice',
'Violet',
'Kendall',
'Morgan',
'Caroline',
'Piper',
'Brooke',
'Elise',
'Alexa',
'Sienna',
'Reese',
'Clara',
'Paige',
'Kate',
'Nevaeh',
'Sadie',
'Quinn',
'Isla',
'Eleanor'
]

lastNames = \
[
'Smith',
'Johnson',
'Williams',
'Jones',
'Brown',
'Davis',
'Miller',
'Wilson',
'Moore ',
'Taylor',
'Anderson',
'Thomas',
'Jackson',
'White ',
'Harris',
'Martin',
'Thompson',
'Garcia',
'Martinez',
'Robinson',
'Clark',
'Rodriguez',
'Lewis',
'Lee',
'Walker',
'Hall',
'Allen',
'Young',
'Hernandez',
'King',
'Wright',
'Lopez',
'Hill',
'Scott',
'Green',
'Adams',
'Baker',
'Gonzalez',
'Nelson',
'Carter',
'Mitchell',
'Perez ',
'Roberts',
'Turner',
'Phillips',
'Campbell',
'Parker',
'Evans ',
'Edwards',
'Collins',
'Stewart',
'Sanchez',
'Morris',
'Rogers',
'Reed',
'Cook',
'Morgan',
'Bell',
'Murphy',
'Bailey',
'Rivera',
'Cooper',
'Richardson',
'Cox',
'Howard',
'Ward',
'Torres',
'Peterson',
'Gray',
'Ramirez',
'James ',
'Watson',
'Brooks',
'Kelly ',
'Sanders',
'Price ',
'Bennett',
'Wood',
'Barnes',
'Ross',
'Henderson',
'Coleman',
'Jenkins',
'Perry',
'Powell',
'Long',
'Patterson',
'Hughes',
'Flores',
'Washington',
'Butler',
'Simmons',
'Foster',
'Gonzales',
'Bryant',
'Alexander',
'Russell',
'Griffin',
'Diaz',
'Hayes',
]

if __name__ == "__main__":
    main(firstNames, lastNames)
