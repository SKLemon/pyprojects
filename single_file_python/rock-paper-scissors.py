##Created as a part of the BAIL repository on Github. Created 01/17/2024

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
print(f"You chose {user_input}")

print(choices[user_input]) # Uses the int assigned as user_input to call the list index of the choices.

# Randomize computer input
computer_input = random.randint(0,2) #This returns an integer
print(f"Computer chose {computer_input}")

print(choices[computer_input]) # Same as above, but for the computer

# Condition for winning or losing
# if user_input == computer_input:
#     print("It's a draw")
# elif user_input < computer_input:
#     print("You lose")
# elif computer_input > user_input:
#     print("You lose!")
# elif user_input == 0 and computer_input == 2:
#     print("You win!")
# elif user_input > computer_input:
#     print("You win!")
# else:
#     print("Invalid choice")