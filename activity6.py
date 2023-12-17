class CoffeeBean:
    def __init__(self, name, origin) -> None:
        self.name = name
        self.origin = origin

    def describe(self):
        print(f"Coffe name: {self.name}\nOrigin: {self.origin}")

class ArabicCoffee(CoffeeBean):
    def __init__(self, name, origin, acidity) -> None:
        super().__init__(name, origin)
        self.acidity = acidity

    def describe(self):
        print(f"Coffe name: {self.name}\nOrigin: {self.origin}\n{self.acidity}")

class RobustaCoffee(CoffeeBean):
    def __init__(self, name, origin, strength) -> None:
        super().__init__(name, origin)
        self.strength = strength

def print_coffee_info(coffee_beans):
    for every_bean in coffee_beans:
        print(f"Name: {every_bean.name}\nOrigin: {every_bean.origin}")

r = RobustaCoffee("Kopiko", "Ph", 100)
a = ArabicCoffee("3in1", "Arab", "kahit ano")

coffee_beans = [r, a]

print_coffee_info(coffee_beans)