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

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealerHand, playerHand):
    clear()
    print("The dealer has a {} for a total of {}".format(dealerHand,total(dealerHand)))
    print("You have a {} for a total of {}".format(playerHand, total(playerHand)))

def play_again():
    option = input("Would you like to play again? (Y/N): ").upper()
    if option == 'Y':
        dealerHand = []
        playerHand = []
        newDeck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
        game()
    else:
        print("Thanks for playing, see you!")
        exit()

def blackjack(dealerHand, playerHand):
    if total(playerHand) == 21:
        print_results(dealerHand, playerHand)
        print("Well done! You got a Blackjack!\n")
        play_again()
    elif total(dealerHand) == 21:
        print_results(dealer_hand, player_hand)
		print("Sorry, dealer got a blackjack... you lose\n")
		play_again()

def score(dealer_hand, player_hand):
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print("Congratulations! You got a Blackjack!\n")
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)
		print("Sorry, dealer got a blackjack... you lose\n")
	elif total(player_hand) > 21:
		print_results(dealer_hand, player_hand)
		print("Sorry. You busted. You lose.\n")
	elif total(dealer_hand) > 21:
		print_results(dealer_hand, player_hand)
		print("Dealer busted. You win!\n")
	elif total(player_hand) < total(dealer_hand):
		print_results(dealer_hand, player_hand)
   		print("Sorry. Your score isn't higher than the dealer. You lose.\n")
	elif total(player_hand) > total(dealer_hand):
		print_results(dealer_hand, player_hand)
		print("Congratulations. Your score is higher than the dealer. You win\n")

def game():
	choice = 0
	clear()
	print "WELCOME TO BLACKJACK!\n"
	dealer_hand = deal(deck)
	player_hand = deal(deck)
	while choice != "q":
		print ("The dealer is showing a {}".format(dealer_hand[0]))
		print("You have a {} for a total of {}".format(playerHand, total(playerHand)))
		blackjack(dealer_hand, player_hand)
		choice = raw_input("Do you want to [H]it, [S]tand, or [Q]uit: ").upper()
		clear()
		if choice == "H":
			hit(player_hand)
			while total(dealer_hand) < 17:
				hit(dealer_hand)
			score(dealer_hand, player_hand)
			play_again()
		elif choice == "S":
			while total(dealer_hand) < 17:
				hit(dealer_hand)
			score(dealer_hand, player_hand)
			play_again()
		elif choice == "Q":
			print "Bye!"
			exit()



# poxis: operating system similar to unix
# nt: new technology / related to windows operating system
