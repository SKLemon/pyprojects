# Created as part of the BAIL repo on Github. Created 12/04/2024

### Blackjack House Rules ###
# The deck is unlimited in size. -> #TO-DO 1: Change this to a deck size of 32 and remove a card each time the call_card function is called
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn. #TO-DO 3: Related to TO-DO 1, removing the cards
# The computer is the dealer.

import time
from art import logo_blackjack
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def call_card(cards, hand, score, num_cards=1):
    """Adds a specific number of cards to the hand, from the cards list, and sums it up
    cards = cards list
    hand = The hand which recieves the card (dealers, yours etc)
    num_cards = number of cards you wish to draw, default is 1
    """
    for var in range(num_cards):
        card = random.choice(cards)
        hand.append(card)

    score = sum(hand)

    if (
        11 in hand and score > 21
    ):  # Replaces the Ace (value of 11) with an Ace (value of 1) to avoid going over 21, for both dealer and user
        hand.remove(11)
        hand.append(1)
        score = sum(hand)

    return score


user_win = True
while user_win == True:

    user_plays = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': "
    ).lower()

    if user_plays == "y":
        your_hand = []
        dealer_hand = []
        your_score = 0
        dealer_score = 0
        your_score = call_card(cards, your_hand, your_score, 2)
        dealer_score = call_card(cards, dealer_hand, dealer_score, 2)

        print("\n" * 20)
        print(logo_blackjack)

        while True:
            if your_score > 21:
                print(
                    f"Bust! Your score is: {your_score}\n The dealer will now shuffle again"
                )
                time.sleep(3)
                break

            elif your_score == 21:
                print(
                    f"You've hit blackjack with a score of {your_score}!\n The dealer will now shuffle again"
                )
                time.sleep(3)
                break

            elif dealer_score > 21:
                print(
                    f"Dealer went bust! Their score is: {dealer_score}\n The dealer will now shuffle again"
                )
                break

            else:
                print(f"Your cards: {your_hand}, current score: {your_score}")
                print(f"Computer's first card: {dealer_hand[0]}")

                user_continue = input(
                    "Type 'y' to get another card, type 'n' to pass: "
                ).lower()

                if user_continue == "y":
                    your_score = call_card(cards, your_hand, your_score)

                elif user_continue == "n":
                    while dealer_score <= 18:
                        dealer_score = call_card(cards, dealer_hand, dealer_score)

                    if dealer_score > 21:
                        print("Dealer drew a card")
                        print(
                            f"Dealer went bust! Their score is: {dealer_score}\n The dealer will now shuffle again"
                        )

                    elif your_score > dealer_score:
                        print(
                            f"You win! \n Your score: {your_score} \n Dealer's Score: {dealer_score}\n Dealer will now shuffle again"
                        )
                        time.sleep(3)
                    elif dealer_score > your_score:
                        print(
                            f"You lose! \n Your score: {your_score} \n Dealer's Score: {dealer_score}\n Dealer will now shuffle again"
                        )
                        time.sleep(3)
                    break
    else:
        user_win = False
        print("Goodbye!")
