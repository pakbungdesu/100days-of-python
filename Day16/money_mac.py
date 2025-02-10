class MoneyMachine:
    def __init__(self):
        self.profit = 0
        self.more = 0
        self.pay = 0

    def report(self):
        print(f"Profit: {self.profit}")

    def check_payment(self, drink):
        if self.pay == drink.cost:
            self.profit += drink.cost
            self.more = 0
        elif self.pay > drink.cost:
            self.profit += drink.cost
            change = round(self.pay - drink.cost, 2)
            print(f"There is ${change} in change.")
            self.more = 0
        else:
            self.more = drink.cost - self.pay
        return self.more

    def make_payment(self, drink):
        self.more = drink.cost
        while self.more > 0:
            print(f"Please insert ${self.more}")
            self.pay += int(input("How many quarters?: ")) * 0.25
            self.pay += int(input("How many dimes?: ")) * 0.1
            self.pay += int(input("How many nickles?: ")) * 0.05
            self.pay += int(input("How many pennies?: ")) * 0.01
            self.more = self.check_payment(drink)

        # reset self.pay
        self.pay = 0
