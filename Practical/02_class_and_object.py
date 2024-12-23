class Person:
    
    def __init__(self):
        self.name = input("enter a name: ")
        self.city = input("enter a cit: ")
      
    
    def Display(self):
        print(f"Your name {self.name} and city {self.city}")

c = Person()
c.Display