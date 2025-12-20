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

    def resources_suff(self, drink):
        """
        Checks if there are enough resources to make a specific drink.

        Args:
            drink (MenuItem): The MenuItem object containing required ingredients.

        Returns:
            bool: True if ingredients are sufficient, False otherwise.
        """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not sufficient {item}.")
                can_make = False
        return can_make

    def make_coffee(self, drink):
        """
        Deducts the required ingredients from the resources and 'brews' the coffee.

        Args:
            drink (MenuItem): The MenuItem object to be produced.
        """
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} ☕️. Enjoy!")
