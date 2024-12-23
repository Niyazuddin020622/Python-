class Programmer():
    company = "Microsoft"
    def __init__(self):
        self.name = input("Enter your name:")
        self.salary = int(input("Enter your salary:"))
        self.pin = int(input("Enter your pincode: "))

    def Display(self):
        print(f"My name is {self.name} my salary {self.salary} and my pincode {self.pin} {self.company}")

pro = Programmer()
pro.Display()

class Programmer():
    company = "Microsoft"
    def __init__(self,name,salary,city):
        self.name = name
        self.salary = salary
        self.city = city

p = Programmer("Harry",12,"Saran")
print(p.name,p.salary,p.city,p.company)