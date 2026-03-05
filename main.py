from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machineOn = True

while machineOn:
    user_input = input("What would you like? (espresso/latte/cappuccino/):")
    if user_input == 'off':
        machinOn = False
        break
