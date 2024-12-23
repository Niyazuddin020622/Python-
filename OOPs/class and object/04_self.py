class Employee():
    name = "Niyazuddin"
    language = "Hindi"
    salary = 120

    def getInfo(self):
        print(f"My name is {self.name} and my language {self.language} and salary {self.salary}")

    # @staticmethod
    def greet(self):
        print("Good Morning!")

niyazu = Employee() # This is an object
niyazu.greet()
niyazu.getInfo()