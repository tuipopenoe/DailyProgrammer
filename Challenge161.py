# Tui Popenoe
# Challenge 161 Blackjack

import random
import sys

deck = [    
        '2S', '2C', '2D', '2H',
        '3S', '3C', '3D', '3H',
        '4S', '4C', '4D', '4H',
        '5S', '5C', '5D', '5H',
        '6S', '6C', '6D', '6H',
        '7S', '7C', '7D', '7H',
        '8S', '8C', '8D', '8H',
        '9S', '9C', '9D', '9H',
        '10S', '10C', '10D', '10H',
        'JS', 'JC', 'JD', 'JH',
        'QS', 'QC', 'QD', 'QH',
        'KS', 'KC', 'KD', 'KH',
        'AS', 'AC', 'AD', 'AH'
        ]

def dealHand(deck):
    count1 = random.randint(0, len(deck)-1)
    card1 = deck.pop(count1)
    print(card1)
    count2 = random.randint(0, len(deck)-1)
    card2 = deck.pop(count2)
    print(card2)

    hand = [card1, card2]
    print(hand)
    return hand

def shuffleDecks(n, deck):
    decks = []
    for i in range(int(n)):
        decks.extend(deck)

    return decks

def calculateBlackjack(n, deck):
    hands = []
    count = 0
    total = 0
    for i in range(int(n)*26):
        hands.extend(dealHand(deck))
        card1 = hands[i][:-1]
        print('Hand: ' + hands[i])
        #print('Card1: ' + card1)
        card2 = hands[i][:-1]
        #print('Card2: ' + card2)
        if card1 == '10':
            if card2 == 'A':
                count += 1
        if card2 == 'A':
            if card2 == '10':
                count += 1
        total += 1

    print(count/total)
    return count / total

def main():
    random.seed()
    n = sys.argv[1]
    print(n)
    decks = shuffleDecks(n, deck)
    calculateBlackjack(n, decks)

if __name__=='__main__':
    main()