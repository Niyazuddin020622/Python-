age = int(input("Enter your age: "))

if age < 13:
    print("You are a child! ")
elif 13 <= age <=19:
    print("You are teanger.")
elif 20 <=age <=64:
    print("Your are adult!")
else:
    print("Your are a senior! ")