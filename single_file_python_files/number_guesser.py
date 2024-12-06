#Created as a part of the BAIL repository on Github. Created/Submitted 12/06/2024

#This one explores functions and scope a bit deeper. The first iteration of this involved changing global vars inside a function (big no no)

import random
from art import logo_guesser
HARD_TURNS = 5
EASY_TURNS = 10

def number_check(guess,randnum,turns):
    if guess > randnum:
        print("Too high.\n Guess again")
        return turns - 1
    elif guess < randnum:
        print("Too low.\n Guess again")
        return turns - 1
    else:
        print(f"You got it! The answer was {randnum}!")

def user_difficulty():
    easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if easy_or_hard == "hard":
        return HARD_TURNS
    else:
        return EASY_TURNS

def game():

    print(logo_guesser)

    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number = (random.randint(1,100))
    print(number)

    #User chooses difficulty
    attempts = user_difficulty()

    #User guesses a number
    user_guess = 0
    while user_guess != number:
        print(f"You have {attempts} attempts to guess the number")
        user_guess = int(input("Make a guess: "))
        attempts = number_check(user_guess,number,attempts)
        if attempts == 0:
            print("Game over, you have no more attempts remaining")
            break
        elif user_guess == number:
            print("Congrats! You guessed correctly!")
            break
game()