class Employee:
    def __init__(self):
        print("Constructor of Employee:")
    a = 1
class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer:")
    b =2
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager:")
    c =3

# obj = Employee()
# print(obj.a)

# obj = Programmer()
# print(obj.a,obj.b)


obj = Manager()
print(obj.a,obj.b,obj.c)


