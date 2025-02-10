from coffee_maker import CoffeeMaker
from menu import Menu
from money_mac import MoneyMachine

# ------------- PIC -------------#

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

# --------------- PROCESS --------------- #

menu = Menu()
coffee_maker = CoffeeMaker()
money_mac = MoneyMachine()

want = input(f"What would you like? (espresso/latte/cappuccino): ").lower()

while want != "off":
    if want == "report":
        money_mac.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(want)
        try:
            suff = coffee_maker.resources_suff(drink)
            if suff:
                money_mac.make_payment(drink)
                coffee_maker.make_coffee(drink)
            else:
                pass
        except AttributeError:
            pass

    want = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
