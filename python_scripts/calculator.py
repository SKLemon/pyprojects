# Created as a part of the BAIL repository on Github. Created 12/02/2024

# Because everybody makes a calculator...right? This mini project dabbles in functions and explores while loops a bit more

from art import logo_calculator


# Defining the operations into functions of the calculator below
def add(n1, n2):
    """Adds 2 user-provided inputs"""
    return n1 + n2


def subtract(n1, n2):
    """Subtracts 2 user-provided inputs"""
    return n1 - n2


def multiply(n1, n2):
    """Multiplies 2 user-provided inputs"""
    return n1 * n2


def divide(n1, n2):
    """Divides 2 user-provided inputs, and checks for division by 0"""
    if n2 != 0:
        return n1 / n2
    else:
        return "Dividing by zero error"


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo_calculator)
    loop = True
    num1 = float(input("What is the first number?: "))

    while loop == True:
        for key in operations:
            print(key)

        user_operation = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        result = float((operations[user_operation](num1, num2)))
        print(f"{num1} {user_operation} {num2} = {result}")

        user_repeat = input(
            f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: "
        )

        if user_repeat == "y":
            num1 = result
        else:
            loop = False
            print("\n" * 20)
            calculator()


calculator()
