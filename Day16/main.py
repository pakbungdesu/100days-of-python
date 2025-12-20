"""
Main controller for the OOP Coffee Machine.
Coordinates the Menu, CoffeeMaker, and MoneyMachine classes to process orders.
"""

from coffee_maker import CoffeeMaker
from menu import Menu
from money_mac import MoneyMachine

# ------------- ASSETS -------------#

logo = """
    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _  | 
    |               |_| |
    |             |\\___/
    \\___________/    
"""

print(logo)

# --------------- INITIALIZATION --------------- #

# Create instances of the classes defined in other modules
menu = Menu()
coffee_maker = CoffeeMaker()
money_mac = MoneyMachine()

# Initial prompt to start the machine loop
want = input(f"What would you like? ({menu.get_items()}): ").lower()

# --------------- MAIN PROGRAM LOOP --------------- #

while want != "off":
    if want == "report":
        # Display current status of resources and money
        coffee_maker.report()
        money_mac.report()
    else:
        # Search for the drink in the menu
        drink = menu.find_drink(want)

        # Check if the drink exists and if resources are sufficient
        try:
            # coffee_maker.resources_suff returns True if ingredients are available
            if coffee_maker.resources_suff(drink):
                # money_mac.make_payment returns True if payment is successful
                if money_mac.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        except AttributeError:
            # Handles cases where menu.find_drink(want) returns None
            pass

    # Repeat the prompt for the next customer
    want = input(f"What would you like? ({menu.get_items()}): ").lower()
