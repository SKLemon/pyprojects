#Created as a part of the BAIL repository on Github. Created 01/14/2024

#This was completed during a demo of the 100 Days of Python Course. Did not do this myself.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
    
    wants_photo = input("Do you want your photo taken? Y or N.")
    if wants_photo == "Y":
      bill += 3
  print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")