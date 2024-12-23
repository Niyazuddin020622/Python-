def goodDay(name):
    print("Good Day, "+ name)
    return "Done"

name = input("Enter your name")

a = goodDay(name)
print(a)


def greet(name,state,city):
    print("Welcome,"+ name)
    print("Your State: "+ state)
    print("Your country:" + city)
    return name,state,city
name = input("Enter your name: ")
state = input("Enter your state")
city = input("Enter your city: ")

a = greet(name,state,city)
print(a)
