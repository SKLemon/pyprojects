#Created as a part of the BAIL repository on Github. Created 01/15/2024

# import random

# Allows to get random whole numbers
# random_integer = random.randint(1,10)
# print(random_integer)

# #Allows to get random decimal numbers between 0 and 1.
# randomFloat = random.random()
# print(randomFloat)

# Also allows to increase the range of random decimal numbers through math operators
# Ex. random_float * 5 would result in a random decimal number between 0 and 5

# ~~~~~ Lists ~~~~~~
# List is a data structure - Another way to store data.
    # - Store data that can be grouped together for organization
    # - Store data that is required to be in a certain order

# Syntax: fruits = [item1, item2, item3]
# Index could also be considered as an offset. For example:
# If you want to get the second fruit item
# print(fruits[0]) would get item1, print{fruit[1]} would get item2, from the above list

# Managing a list
    # Changing items from a list: fruits[index] = Changed item name. EX fruit[0] = "Strawberry" would change the first item to strawberry
    # Adding a single item to a list: fruits.append("Object to add on")
    # Extending a list by adding multiple items: fruit.extend([item1, item2, item3, etc])
# Nested Lists
    # List in a list
    # Set your list first. EX. Set your list variables - variable1 = [item1, item2, item3] variable2 = [item4, item5, item6] 
    # nested_list = [variable1, variable2]. Can also occur as nested_list = [variable1][variable2]

# Testing code

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])

# below is the code for placing an X on a user defined area in a list

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("B3") # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# First convert the first input to an index.
letter = position[0] # Grabs the first input from user
var = ["A", "B", "C"] # Assigns any of the choices the user could have made to a list variable in the same order as the map
letter_index = var.index(letter) # Assigns the letter to an index based on the way the list was created for var, above
 
 # Second, convert the second input into an index
number_index = int(position[1]) - 1 # Since the second input from user is a number, we simply convert to an integer and subtract one to match it with the index

# We now have both inputs from the user converted to an index that is readable by the nested map list
map[number_index][letter_index] = "X" # So we assign the location to an "X" as required
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}") # This line prints out the updated map with the X in the correct location based on user input