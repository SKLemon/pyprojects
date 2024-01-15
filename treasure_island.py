# Multiple choice adventure mini-game set in the terminal.
# 
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# Starting Condition
user_input1 = input("You are at a crossroad. Where do you want to go? Type 'left' or right'\n").lower()

# Winning Condition
if user_input1 == "left":
  print("You have reached the river\n")
  user_input2 = input("Do you want to swim or wait for the boat? Type 'swim' or 'wait'\n").lower()
  if user_input2 == "wait":
    print("You have crossed the river safely and reached the island.\n")
    user_input3 = input("You have three doors in front of you. Which one do you choose? Type 'Red, Blue, or Yellow'\n").lower()
    if user_input3 == "yellow":
      print("Congratulations! The yellow door leads to the treasure. You win!\n")
# All other specific losing conditions noted with keywords
    elif user_input3 == "red" or user_input3 == "blue":
      print("Wrong door! You fell to your death. Game over.")
    else: #all other losing conditions encapsulated in here
      print("Even you didn't understand what you said so you walked around endlessly in a circle contemplating the meaning of following instructions until you died of exhaustion... Game over.")
  elif user_input2 == "swim":
    print("You were attacked by a school of angry trouts. Game over.")
  else: #all other losing conditions encapsulated in here
    print("Even you didn't understand what you said so you walked around endlessly in a circle contemplating the meaning of following instructions until you died of exhaustion... Game over.")
elif user_input1 == "right":
  print("You fell into a hole. Game over.")
else: #all other losing conditions encapsulated in here
  print("Even you didn't understand what you said so you walked around endlessly in a circle contemplating the meaning of following instructions until you died of exhaustion... Game over.")