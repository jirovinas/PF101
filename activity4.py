class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def speak(self):
        print(f"{self.name} is an {self.species} and makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
    def speak(self):
        print(f"{self.name} is a {self.breed} dog and barks.")
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color
    def speak(self):
        print(f"{self.name} is a {self.color} cat and meows.")

dog = Dog("Buddy","Golden Retriever")
cat = Cat("Whiskers","Gray")

dog.speak()
cat.speak()