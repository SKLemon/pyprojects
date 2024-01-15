#Created as a part of the BAIL repository on Github. Created 01/24/2024

# Checking a user input to see if the number they provided is odd or even
number = int(input("Please enter your number to check if it's even or odd\n"))
if number % 2 == 0: #Checks for remainder of the number. If a remainder exists after being divided by 2, it is an odd number
    print(f"Your number {number} is even")
else:
    print(f"Your number {number} is odd")