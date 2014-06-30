# Tui Popenoe
# Challenge 159 Rock Paper Scissors Lizard Spock

"""
    Implementation of Rock, Paper, Scissors, Lizard, Spock game.
    Accepts player input until the player decides to quit.
"""

hands = ['R', 'P', 'S', 'L', 'K']

handsDict = {
    'R' : 'Rock',
    'P' : 'Paper',
    'S' : 'Scissors', 
    'L' : 'Lizard',
    'K' : 'Spock'
}

def main():
    choice = raw_input()
    hwins = 0
    cwins = 0
    ties = 0
    total = 0

    while choice != 'quit':
