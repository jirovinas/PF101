class MenuItem:
    def __init__(self, item_name, price, description) -> None:
        self.__item_name = item_name
        self.__price = price
        self.__description = description

    def display_details(self):
        print(f"Item name: {self.get_description()} \nPrice: ${self.get_price()} \nDescription: {self.get_description()}\n")

    def get_price(self):
        return self.__price

    def get_item_name(self):
        return self.__item_name

    def get_description(self):
        return self.__description
    
    def update_price(self, item_name = None, price = None, description = None):
        if item_name is not None:
            self.__item_name = item_name
            msg += f"Item Name Updated to {item_name}"

        if price is not None:
            self.__price = price
            msg += f"Price Updated to {price}"

        if description is not None:
            self.__description = description
            msg += f"Description Updated to {description}"

    msg = " "
    print(msg)

class Order:
    def __init__(self, name):
        self.name = name
        self.order_list = []

    def add_item(self, order_name):
        if order_name.get_status():
            self.order_list.append(order_name)
            print(f"Order Name: {order_name.get_item_name()}")

    def calculate_total(self):
        total = 0
        for every_order in self.order_list:
            total += every_order.get_price()
        print(f"Total Price: ${total}")

class FoodItem(MenuItem):
    def __init__(self, item_name, price, description, cook = False) -> None:
        super().__init__(item_name, price, description)
        self.cook = cook

    def cook_food(self):
        self.cook = True
        print(f"The {self.get_item_name()} has been cooked")

    def get_status(self):
        return self.cook

class DrinkItem(MenuItem):
    def __init__(self, item_name, price, description, pour = False) -> None:
        super().__init__(item_name, price, description)
        self.pour = True

    def pour_drink(self):
        self.pour = True
        print(f"The {self.get_item_name()} has been poured")

    def get_status(self):
        return self.pour

class PremiumFoodItem(FoodItem):
    def __init__(self, item_name, price, description, cook=False) -> None:
        super().__init__(item_name, price, description, cook)

class PremiumFoodItem(DrinkItem):
    def __init__(self, item_name, price, description, pour=False) -> None:
        super().__init__(item_name, price, description, pour)

pizza = FoodItem("Pizza", 100, "Large")
pizza.cook_food()
pizza.display_details()
hagsxxh = ''
order1 = Order("Jiro")
order1.add_item(pizza)
order1.calculate_total()