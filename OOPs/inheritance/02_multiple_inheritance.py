class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company} ")
    
class Coder:
        language ="Python"
        def printlanguage(self):
            print(f"Out of all the languages here is your language: {self.language} ")

class Programmer(Employee,Coder):
     company = "ITC comapny"
     def showlanguage(self):
          print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printlanguage()
b.showlanguage()

