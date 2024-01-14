# Checking a user input to see if the number they provided is odd or even
number = int(input())
if number % 2 == 0: #Checks for remainder of the number. If a remainder exists after being divided by 2, it is an odd number
    print(f"Your number {number} is even")
else:
    print(f"Your number{number} is odd")