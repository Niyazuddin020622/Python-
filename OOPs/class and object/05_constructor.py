class Person():
    def __init__(self,name,salary,lang):
        self.name = name
        self.salary = salary
        self.lang = lang

        print(f"I am creating object!")

    def Display(self):
        print(f"{self.name}, {self.salary}, {self.lang}")

niyazu = Person("Niyazud",10000,"JavaScript") # this is constructor called pass parameters
# niyazu.Person()

print(niyazu.name,niyazu.salary,niyazu.lang)