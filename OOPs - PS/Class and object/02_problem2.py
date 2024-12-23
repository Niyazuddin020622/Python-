class Calculator:
    def __init__(self):
        self.number = int(input("Enter a number: "))

    def square(self):
        print(f"The square is {self.number * self.number}")

    def cube(self):
        print(f"The cube is {self.number * self.number * self.number}")

    def squareroot(self):
        print(f"The square root is {self.number ** 0.5}")


c = Calculator()
c.square()
c.cube()
c.squareroot()
