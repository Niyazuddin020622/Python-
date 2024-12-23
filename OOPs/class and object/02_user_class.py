class Person(): # This is class
    def __init__(self): # dunder method wich is automatically called
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.salary = int(input("Enter your salary: "))

    def Display(self):
        print(f"Name: {self.name}, Age: {self.age}, your Salary: {self.salary}")

person = Person() # This is an object
person.Display()