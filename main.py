from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker_obj = CoffeeMaker()
money_machine_obj =  MoneyMachine()
menu = Menu()

machineOn = True
while machineOn:
    options = menu.get_items()
    choice = input(f"What would you like? {options}:")
    if choice == 'off':
        machinOn = False
        break
    elif choice == 'report':
        coffee_maker_obj.report()
        money_machine_obj.report()
    
    else:
        drink = menu.find_drink(choice)
        print(coffee_maker_obj.is_resource_sufficient(drink))
    

