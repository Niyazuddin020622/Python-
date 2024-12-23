class Employee:
    a = 1
class Programmer(Employee):
    b = 2
class Manager(Programmer):
    c = 3

# Get user input for the class type

user_input = input("Enter the class you want to create an object of (Employee,Programmer,Manager): ".strip())

if user_input == "Employee":
    obj = Employee()
    print(f"Employee object: a = {obj.a}")
elif user_input == "Programmer":
    obj = Programmer()
    print(f"Programmer object: a = {obj.a}, b = {obj.b}")
elif user_input == "Manager":
    obj = Manager()
    print(f"Manager object: a = {obj.a}, b = {obj.b}, c = {obj.c}")
else:
    print("Invalid class name entered!")

    