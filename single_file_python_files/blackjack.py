# Created as part of the BAIL repo on Github. Created 12/04/2024

### Blackjack House Rules ###
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from art import logo_blackjack
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def call_card(cards, hand, num_cards=1):
    """Adds a specific number of cards to the hand, from the cards list
    cards = cards list
    hand = The hand which recieves the card (dealers, yours etc)
    num_cards = number of cards you wish to draw, default is 1
    """
    for var in range (num_cards):
        card = random.choice(cards)
        hand.append(card)
# Ask user to play - Possibly a while loop continously asking until no

def blackjack():
    user_win = True
    user_plays = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if user_plays == "y":
        your_hand = []
        dealer_hand = []
        your_score = 0
        dealer_score = 0
        
        call_card(cards,your_hand,2)
        call_card(cards,dealer_hand,2)
    else:
        print("Goodbye")
        user_plays = "n"

    while user_plays == "y" and user_win == True:
        print("\n" * 20)
        print(logo_blackjack)

        for card in your_hand:
            your_score += card
        for card in dealer_hand:
            dealer_score += card

        if your_score > 21:
            print(f"Bust! Your score is: {your_score}")
            user_win = False
            blackjack()
        if your_score == 21:
            print("You win!")
            blackjack()

        print(f"Your cards: {your_hand}, current score: {your_score}")
        print(f"Computer's first card: {dealer_hand[0]}")

        user_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if user_continue == "y":
            call_card(cards,your_hand)
            call_card(cards,dealer_hand)
            if your_score > 21:
                print(f"Bust! Your score is: {your_score}")
                user_win = False
                blackjack()
        else:
            if dealer_score < 21:
                call_card(cards,dealer_hand)

blackjack()