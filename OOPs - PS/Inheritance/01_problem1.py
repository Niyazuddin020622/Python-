# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child Class 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Child Class 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Child Class 3 (inherits and extends functionality)
class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)  # Inheriting from the parent class
        self.can_fly = can_fly

    def speak(self):
        return f"{self.name} says Chirp!"

    def flight_ability(self):
        return f"{self.name} {'can fly' if self.can_fly else 'cannot fly'}."
    

# Create objects for each class
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety", True)

# Access methods
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
print(bird.speak())  # Output: Tweety says Chirp!
print(bird.flight_ability())  # Output: Tweety can fly.
