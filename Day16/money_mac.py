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

    def check_payment(self, drink):
        """
        Calculates if the money inserted is enough for the drink.

        Args:
            drink (MenuItem): The drink object containing the cost.

        Returns:
            float: The remaining amount still owed. Returns 0 if fully paid.
        """
        if self.pay == drink.cost:
            self.profit += drink.cost
            self.more = 0
        elif self.pay > drink.cost:
            self.profit += drink.cost
            change = round(self.pay - drink.cost, 2)
            print(f"There is {self.CURRENCY}{change} in change.")
            self.more = 0
        else:
            self.more = round(drink.cost - self.pay, 2)
        return self.more

    def make_payment(self, drink):
        """
        Prompts the user to insert coins until the drink cost is met.

        Args:
            drink (MenuItem): The drink object the user wants to buy.
        """
        self.more = drink.cost
        while self.more > 0:
            print(f"Please insert {self.CURRENCY}{self.more}")
            # Process coin inputs and update current payment total
            self.pay += int(input("How many quarters?: ")) * self.COIN_VALUES["quarters"]
            self.pay += int(input("How many dimes?: ")) * self.COIN_VALUES["dimes"]
            self.pay += int(input("How many nickles?: ")) * self.COIN_VALUES["nickles"]
            self.pay += int(input("How many pennies?: ")) * self.COIN_VALUES["pennies"]

            self.more = self.check_payment(drink)

        # Reset the temporary payment variable for the next customer
        self.pay = 0
