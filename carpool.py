class Vehicle:
    def __init__(self, name, capacity, fare_per_kilometer, driver, customers) -> None:
        self.name = name
        self.capacity = capacity
        self.fare_per_kilometer = fare_per_kilometer
        self.driver = None
        self.customers = []
        self.totalfare = 0


    def assign_driver(self, driver):
        print(f"Driver {driver.name} is assigned to {self.name}")
        print("\n")

    def add_customer(self, customer):
        if len(self.customers) != self.capacity:
            self.customers.append(customer)
            print(f"Customer {customer.name} is added to the vehicle {self.name}")
        else:
            print("Error: aximum capacity reached")
            print("\n")

    def calculate_fare(self, km):
        self.km = km
        self.totalfare = self.km * self.fare_per_kilometer
        
    def get_trip_info(self):
        for every_name in self.customers:
            print(f"Customer {every_name.name} at vehicle {self.name}")
        print(f"Every customer will have to pay the fares of {self.totalfare}")

        index = 0
        for every_customer in self.customers:
            index += 1
            print(f" The customer {every_customer.name} is in seat {index}")

class Driver:
   def __init__(self, name, license_number) -> None:
       self.name = name
       self.license_number = license_number




class Customer:
    def __init__(self, name, phone_number) -> None:
        self.name = name
        self.phone_number = phone_number

vehicle1 = Vehicle("Toyota", 4, 20, "", "")

manong = Driver("Natoy", 123)

customer1 = Customer("A", 123456789)
customer2 = Customer("B", 123456789)
customer3 = Customer("C", 123456789)
customer4 = Customer("D", 123456789)
customer5 = Customer("E", 123456789)

vehicle1.assign_driver(manong)
vehicle1.add_customer(customer1)
vehicle1.add_customer(customer2)
vehicle1.add_customer(customer3)
vehicle1.add_customer(customer4)
vehicle1.add_customer(customer5)

vehicle1.calculate_fare(20)
vehicle1.get_trip_info()
