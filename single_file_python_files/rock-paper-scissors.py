##Created as a part of the BAIL repository on Github. Created 01/17/2024

# Update: 12/08... Wouldn't functions for this whole mess be so much easier?

# Rock Paper Scissors, chosen at random by the computer. Need to import "random"
import random

#Insert ASCII Art below and place them in variables to get called when needed

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors] # Assigns the ASCII art above into table format for index call

# Get User's input
user_input = int(input("Choose Rock (0), Paper (1), or Scissors (2)\n")) #Converted to int as it will print a string

#Update: Fixing below code a bit with a while loop
while user_input >=3 or user_input < 0:
    user_input = int(input("Invalid choice. Choose Choose Rock (0), Paper (1), or Scissors (2)\n")

choices_user = choices[user_input]
print(choices[user_input]) # Uses the int taken from user_input to call the list index of the choices... Because the user input happens to be the same as a list index.

# Randomize computer input
computer_input = random.randint(0,2)
print(f"Computer chose:")

choices_computer = choices[computer_input]

print(choices[computer_input])

# Condition for winning or losing
# There's got to be a better solution for this... Too many if statements
if choices_user == choices_computer:
    print("It's a draw")
elif choices_user == rock and choices_computer == scissors:
    print("You win!")
elif choices_user == rock and choices_computer == paper:
    print("You lose!")
elif choices_user == scissors and choices_computer == rock:
    print("You lose!")
elif choices_user == scissors and choices_computer == paper:
    print("You win!")
elif choices_user == paper and choices_computer == scissors:
    print("You lose!")
elif choices_user == paper and choices_computer == rock:
    print("You win!")
else:
    print("Invalid Choice")