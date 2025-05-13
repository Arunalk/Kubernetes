from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
drink = Menu()
money = MoneyMachine()
money.report()
coffee_maker.report()
exit = True
while exit:
    choice = input("What drink would u like to have\n")
    if choice == "off":
        exit = False
    elif choice == "report":
        money.report()
        coffee_maker.report()
    else:
        beverage = drink.find_drink(choice)
        if coffee_maker.is_resource_sufficient(beverage) and money.make_payment(beverage.cost):
            coffee_maker.make_coffee(beverage)
