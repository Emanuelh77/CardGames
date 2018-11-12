#BLACKJACK

import random
import os

#initializing deck
deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4

higher_cards = ['J', 'Q', 'K']

#deal cards function
def deal(deck):
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
        hand.append(card)
    return hand

#returns the total of the hand
def hand_total(hand):
    total = 0
    for card in hand:
        if card in higher_cards:
            total += 10
        elif card == 'A':
            if total >= 11:
                total += 1
            else: total += 11
        else:
            total += card
    return total

#adds one more card to the hand
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

#clears the terminal window depending on the OS
def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

#function displays the hands of the dealer and player
def print_results(dealerHand, playerHand):
    #clear()
    print("The dealer has a" + str(dealerHand) + " for a total of " + str(hand_total(dealerHand)))
    print("You have a " + str(playerHand) + " for a total of " + str(hand_total(playerHand)))

#restart game
def play_again():
    option = input("Would you like to play again? (Y/N): ").upper()
    if option == 'Y':
        global deck
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        game()
    else:
        print("Thanks for playing, see you!")
        exit()

#this function takes care of the case either dealer or
#player have blackjack
def blackjack(dealerHand, playerHand):
    if hand_total(playerHand) == 21:
        print_results(dealerHand, playerHand)
        print("Well done! You got a Blackjack!\n")
        play_again()
    elif hand_total(dealerHand) == 21:
        print_results(dealerHand, playerHand)
        print("Sorry, dealer got a blackjack... you lose\n")
        play_again()

#this function display the results according to the hands
#both the player and dealer have
def score(dealerHand, playerHand):
    if hand_total(playerHand) == 21:
        print_results(dealerHand, playerHand)
        print("Congratulations! You got a Blackjack!\n")
    elif hand_total(dealerHand) == 21:
        print_results(dealerHand, playerHand)
        print("Sorry, dealer got a blackjack... you lose\n")
    elif hand_total(playerHand) > 21:
        print_results(dealerHand, playerHand)
        print("Sorry. You busted. You lose.\n")
    elif hand_total(dealerHand) > 21:
        print_results(dealerHand, playerHand)
        print("Dealer busted. You win!\n")
    elif hand_total(playerHand) < hand_total(dealerHand):
        print_results(dealerHand, playerHand)
        print("Sorry. Your score isn't higher than the dealer. You lose.\n")
    elif hand_total(playerHand) > hand_total(dealerHand):
        print_results(dealerHand, playerHand)
        print("Congratulations. Your score is higher than the dealer. You win\n")
    elif hand_total(playerHand) == hand_total(dealerHand):
        print("It's a tie!")

#run game function
def game():
    choice = 0
    clear()
    print("WELCOME TO BLACKJACK!\n")
    dealerHand = deal(deck)
    playerHand = deal(deck)
    while choice != "q":
        print("The dealer is showing a {}".format(dealerHand[0]))
        print("You have a " + str(playerHand) + " for a total of " + str(hand_total(playerHand)))
        blackjack(dealerHand, playerHand)
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        if choice == "h":
            hit(playerHand)
            while hand_total(dealerHand) < 17:
                hit(dealerHand)
            score(dealerHand, playerHand)
            play_again()
        elif choice == "s":
            while hand_total(dealerHand) < 17:
                hit(dealerHand)
            score(dealerHand, playerHand)
            play_again()
        elif choice == "q":
            print("Bye!")
            exit()


if __name__ == '__main__':
    game()



# poxis: operating system similar to unix
# nt: new technology / related to windows operating system
