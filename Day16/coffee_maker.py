class CoffeeMaker:
    def __init__(self):
        self.resources = {"water": 300,
                          "milk": 200,
                          "coffee": 100,
                          }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def resources_suff(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not sufficient {item}.")
                can_make = False
        return can_make

    def make_coffee(self, drink):
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} ☕️. Enjoy!")
