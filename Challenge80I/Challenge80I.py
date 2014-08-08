# Tui Popenoe
# Challenge80I.py - Poker Hands
cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

suit = ['S', 'C', 'D', 'H']

hands = {
    'Royal Flush': False,
    'Straight Flush' : False,
    'Four of a Kind' : False,
    'Full House' : False,
    'Flush' : False,
    'Straight' : False,
    'Three of a Kind' : False,
    'Two Pair' : False,
    'Pair' : False,
    'High Card' : False
}

def read_hand(hand):
    h = hand.split()
    ranks = list()
    suits = list()
    for i in h:
        ranks.append(i[0])
        suits.append(i[1])

    s_ranks = ranks.sort()

    for key in suit:
        # Flush
        if suits.count(key) == 5:
            # Royal Flush
            if sorted(ranks) == sorted(cards[-5]):
                hands['Royal Flush'] = True
            # Straight Flush
            if sorted(ranks) == \
                sorted(cards[int(min(ranks))-1:int(min(ranks))+4]):
                hands['Straight Flush'] = True
            hands['Flush'] = True
    for j in cards:
        # Four of a Kind
        if s_ranks.count(j) == 4:
            hands['Four of a Kind'] = True
        if s_ranks.count(j) == 3:
            if s_ranks[2] == s_ranks[3] == s_ranks[4]:
                hands['Full House'] = True
            else:
                hands['Three of a Kind'] = True
        if s_ranks.count(j) == 2:
            if s_ranks[2] == s_ranks[3] == s_ranks[4]:
                hands['Full House'] = True
            if s_ranks[2] == s_ranks[3] or s_ranks[3] == s_ranks[4]:
                hands['Two Pair'] = True
            hands['Pair'] = True
        hands['High Card'] = True

    # Straight
    if sorted(cards[int(min(ranks))-1:int(min(ranks))+4]):
        hands['Straight'] == True

    for key, value in hands.iteritems():
        if value == True:
            return key

    return 'High Card'

def main():
    