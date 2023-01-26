from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

if __name__ == "__main__":
    money = MoneyMachine()
    coffee = CoffeeMaker()
    menu = Menu()
    # infinity loop for next person
    while True:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ")
        if options == "off":
            break
        elif options == "report":
            coffee.report()
            money.report()
        else:
            drink = menu.find_drink(choice)
            if coffee.is_resource_sufficient(drink):
                money.make_payment(drink.cost)
                if money.make_payment(drink.cost) and coffee.is_resource_sufficient(drink):
                    coffee.make_coffee(drink)
