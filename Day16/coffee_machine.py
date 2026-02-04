class CoffeeMaker:
    """
    Models the hardware of the coffee machine responsible for
    managing ingredients and brewing drinks.
    """

    def __init__(self):
        """Initializes the machine with a fixed amount of resources."""
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all current resource levels."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def enough_resource(self, drink):
        """
        Checks if there are enough resources to make a specific drink.

        Args:
            drink (MenuItem): The MenuItem object containing required ingredients.

        Returns:
            bool: True if ingredients are sufficient, False otherwise.
        """
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_coffee(self, drink):
        """
        Deducts the required ingredients from the resources and 'brews' the coffee.

        Args:
            drink (MenuItem): The MenuItem object to be produced.
        """
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} ☕️. Enjoy!")


class MoneyMachine:
    """
    Handles the financial transactions of the coffee machine,
    including coin processing and profit tracking.
    """
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        """Initializes profit and temporary payment variables to zero."""
        self.profit = 0
        self.more = 0
        self.pay = 0

    def report(self):
        """Prints the total profit earned by the machine."""
        print(f"Profit: {self.CURRENCY}{self.profit}")

    def check_payment(self, cost):
        """
        Calculates if the money inserted is enough for the drink.

        Args:
            cost: Cost of drink object the user wants to buy.

        Returns:
            float: The remaining amount still owed. Returns 0 if fully paid.
        """
        if self.pay >= cost:
            change = round(self.pay - cost, 2)
            if change > 0:
                print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            return True
        return False

    def make_payment(self, cost):
        """
        Prompts the user to insert coins until the drink cost is met.

        Args:
            cost: Cost of drink object the user wants to buy.

        Returns:
            bool: True if paid successfully, False otherwise.
        """
        while self.pay < cost:
            remaining = round(cost - self.pay, 2)
            print(f"Total needed: {self.CURRENCY}{remaining}")
            try:
                self.pay += int(input("How many quarters?: ")) * self.COIN_VALUES["quarters"]
                self.pay += int(input("How many dimes?: ")) * self.COIN_VALUES["dimes"]
                self.pay += int(input("How many nickles?: ")) * self.COIN_VALUES["nickles"]
                self.pay += int(input("How many pennies?: ")) * self.COIN_VALUES["pennies"]

                if self.check_payment(cost):
                    self.pay = 0  # Reset for next transaction
                    return True
            except ValueError:
                print("Invalid input. Machine returns previous coins. Please try again.")
                break

        self.pay = 0  # Reset for next transaction
        return False

class MenuItem:
    """
    Models each Menu Item.

    Attributes:
        name (str): The name of the drink.
        cost (float): The price of the drink.
        ingredients (dict): A dictionary of the required ingredients (water, milk, coffee).
    """

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


class Menu:
    """Models the Menu with several menu items."""

    def __init__(self):
        # A list of MenuItem objects
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """
        Returns all the names of the available menu items as a concatenated string.

        Returns:
            str: A string of drink names separated by slashes (e.g., "latte/espresso/").
        """
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """
        Searches the menu for a particular drink by name.

        Args:
            order_name (str): The name of the drink the user wants.

        Returns:
            MenuItem: If the drink exists, returns the MenuItem object.
            None: If the drink does not exist.
        """
        for item in self.menu:
            if item.name == order_name:
                return item
        return None

def process():
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
    want = input(f"What would you like? ({menu.get_items()}): ")

    # --------------- MAIN PROGRAM LOOP --------------- #

    while want != "off":
        if want == "report":
            coffee_maker.report()
            money_mac.report()
        else:
            drink = menu.find_drink(want.lower())
            if drink:
                # Step 1: Check Resources
                if coffee_maker.enough_resource(drink):
                    # Step 2: Handle Money
                    if money_mac.make_payment(drink.cost):
                        # Step 3: Deduct ingredients
                        coffee_maker.make_coffee(drink)
            else:
                print("Sorry, that item is not on the menu.")

        want = input(f"\nWhat would you like? ({menu.get_items()}): ")


if __name__ == "__main__":
    process()
