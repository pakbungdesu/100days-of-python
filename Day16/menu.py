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
        print("Sorry, the item is not available.")
        return None
