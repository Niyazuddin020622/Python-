class Employee:
    a = 1
class Programmer(Employee):
    b = 2
class Manager(Programmer):
    c = 3

o = Employee() # this is object
print(o.a)

o = Programmer()
print(o.a,o.b)

o = Manager()
print(o.a,o.b,o.c)