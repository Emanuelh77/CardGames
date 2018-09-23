from random import *
from os import *

full_deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4

higherCards = ['J', 'Q', 'K']

def deal(full_deck):
    hand = []
    for i in range(0,2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = 'J'
        elif card == 12:
            card = 'Q'
        elif card == 13:
            card = 'K'
        elif card == 14:
            card = 'A'
        else:
            hand.append(card)
    return hand

def hand_total(hand):
    total = 0
    for card in hand:
        if card in higherCards:
            total += 10
        elif card == 'A':
            if total >= 11:
                total += 1
            else:
                total += card
    return total

def hit(hand):
    card = deck.pop()
    if card == 11:
        card = 'J'
    elif card == 12:
        card = 'Q'
    elif card == 13:
        card = 'K'
    else:
        card = 'A'
    hand.append(card)
    return hand


# poxis: operating system similar to unix
# nt: new technology / related to windows operating system
