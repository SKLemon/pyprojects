from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
coffee_menu = Menu()
money_in = MoneyMachine()
machine_on = True

while machine_on == True:
    #Awaits user input, 2 hidden functions ('off', and 'report')

    user_input = input("What would you like to order? Latte, Espresso, or Cappuccino?: ").lower()

    if user_input in coffee_menu.get_items():
        coffee_item = coffee_menu.find_drink(user_input)
        enough_ingredients = coffee.is_resource_sufficient(coffee_item)

        if enough_ingredients == True:
            enough_money = money_in.make_payment(coffee_item.cost)

            if enough_money == True:
                coffee.make_coffee(coffee_item)

    elif user_input == "off":
        machine_on = False

    elif user_input == "report":

        coffee.report()
        money_in.report()
