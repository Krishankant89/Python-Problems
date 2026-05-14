class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water" : water,
            "milk" : milk,
            "coffee": coffee
        }
        
class Menu:
    def __init__(self):
        self.menu=[
            MenuItem(name = "latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name = "Espresso", water = 150, milk = 100, cost = 5.60),
            MenuItem(name = "Cappuccino", water = 100, milk = 140, cost = 4.50)
        ]
