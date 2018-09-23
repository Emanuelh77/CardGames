from enum import Enum
from enum import IntEnum
from random import *

full_deck = []
partial_deck = []
player1_cards = []
player2_cards = []

# this is the card enum for playing cards
class Card(IntEnum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

# suit enum for playing cards
class Suit(Enum):
    Spades = 'spades'
    Clubs = 'clubs'
    Hearts = 'hearts'
    Diamonds = 'diamonds'

# this class holds the information of the playing cards
class PlayingCard:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit

# function to deal full deck of cards
def create_deck():
    for suit in Suit:
        for card in Card:
            full_deck.append(PlayingCard(Card(card),Suit(suit)))
    return full_deck

# function that draws single card from deck
def draw_card(deck):
    randomCard = randint(0,len(deck) - 1)
    return deck.pop(randomCard)

# deal two players 2 decks for the game of war
def deal_war():
    while(len(partial_deck) > 0):
        player1_cards.append(draw_card(partial_deck))
        player2_cards.append(draw_card(partial_deck))

create_deck()
partial_deck = list(full_deck)
deal_war()

print(full_deck)

for i in range(0, len(player1_cards)):
    if player1_cards[i].card > player2_cards[i].card:
        print("Player 1 wins with: ", player1_cards[i].card.name)
        print("Player 2 loses with: ", player2_cards[i].card.name)
        print('\n')
    if player2_cards[i].card > player1_cards[i].card:
        print("Player 2 wins with: ", player2_cards[i].card.name)
        print("Player 1 loses with: ", player1_cards[i].card.name)
        print('\n')
    else:
        print("WAR!\n")






# for i in range(0,len(full_deck)):
#     print('Card: ', full_deck[i].card)
#     print('Suit: ', full_deck[i].suit)
