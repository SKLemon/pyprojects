import time
from data import MENU, resources

# COMPLETED TODO's:
# TODO : 1) Print a report
# TODO : 2) Check resources are sufficient

def format_report(resources):
    """Prints the formatted report

    Args:
        resources (dict): values of 'water', 'coffee', 'milk'
    """
    for ingredient, quantity in resources.items():
        if ingredient in ['water','milk']:
            unit = "ml"
        else:
            unit = "g"
        print(f"{ingredient.title()}: {quantity}{unit}")

def resource_check(resources,required_ingredients):
    """This functions checks a dictionary against another and checks if you have enough

    Args:
        resources (dict): Resources currently on hand
        required_ingredients (dict): Required ingredients. MENU goes here
    Returns:
        bool: True is resources are sufficient, False otherwise
    """
    
    for ingredient,quantity in required_ingredients.items():
        if ingredient not in resources or resources[ingredient] < quantity:
            print(f"Sorry, there is not enough {ingredient}")
            return False
        return True
# Function to get each coin placed in by user, then output total_amount of coins to match up with cost
def coins():
    cash_in = {}
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    total_amount = 0
    cash_in[quarters] = int(input("How many quarters?: "))
    cash_in[dimes] = int(input("How many dimes?: "))
    cash_in[nickles] = int(input("How many nickles?: "))
    cash_in[pennies] = int(input("How many pennies?: "))
    
    for key,val in cash_in.items():
        print(f"{key}: {val}")
        total_amount += val

    return total_amount


accumulated_money = 0.00

machine_on = True
while machine_on == True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input in ["espresso", "latte", "cappuccino"]:

        required_ingredients = MENU[user_input]["ingredients"]
        enough_ingredients = resource_check(resources, required_ingredients)

        if enough_ingredients == True:

            print("Please insert coins.")
            total_amount = coins()
            print (total_amount)

            # If statement on enough coins matching the cost of the drink
            print("Making your drink.... please wait")
            time.sleep(3)
            print("*DING* Enjoy!")

    elif user_input == "off":
        machine_on = False

    elif user_input == "report":
        format_report(resources)
        print(f"Money: ${accumulated_money}")



# TODO: 3) Process coins
# 3a) Coin operated only. Checks how much money was put in using amount of quarters, nickels, dimes, and pennies
# TODO: 4) Check transaction successful
# 5) Make coffee, and keep track of amount of money made
