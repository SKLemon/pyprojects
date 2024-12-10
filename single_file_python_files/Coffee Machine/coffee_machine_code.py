import time
from data import MENU, resources

# COMPLETED TODO's:
# TODO : 1) Print a report
# TODO : 2) Check resources are sufficient
# TODO : 3) Process coins
# TODO : 4) Check transaction successful

def format_report(resources):
    """Prints the formatted report.

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
    """Checks items in a dictionary against another dict and compares.

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

def resource_removal(resources,required_ingredients):
    """Removes the items used from a total.

    Args:
        resources (dict): _description_
        required_ingredients (dict): _description_
    """
    for ingredient,quantity in required_ingredients.items():
        resources[ingredient] -= quantity


def coins(cash_in):
    """Asks user the QUANTITY of coins they are putting in, and outputs its equivalent in money value

    Args:
        cash_in (dict): Dictionary of coins and they're respective currency amounts

    Returns:
        accumulated_money (float): Returns the running total amount of money th_description_
    """
    total_coin_input = 0

    for currency,value in cash_in.items():
        user_cash = int(input(f"How many {currency}?: "))
        total_coin_input += (value * user_cash)

    return total_coin_input

##########################################################

machine_on = True

profit = 0
cash_in = {"quarters": 0.25,
            "dimes": 0.10,
            "nickles": 0.05,
            "pennies": 0.01,
            }

while machine_on == True:

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input in ["espresso", "latte", "cappuccino"]:

        required_ingredients = MENU[user_input]["ingredients"]
        enough_ingredients = resource_check(resources, required_ingredients)

        if enough_ingredients == True:

            print("Please insert coins.")

            accumulated_money = float(coins(cash_in))

            required_money = MENU[user_input]["cost"]

            if accumulated_money < required_money:
                print("Sorry, that's not enough money. Money refunded.")

            elif accumulated_money >= required_money:
                change = accumulated_money - required_money

                print(f"Here is ${change:.2f} in change")

                profit += required_money

                resource_removal(resources,required_ingredients)

    elif user_input == "off":
        machine_on = False

    elif user_input == "report":
        format_report(resources)
        print(f"Money: ${profit}")
