number = int(input("Enter your Number: "))

if (number%2==0):
    print("The numbe is even")
else:
    print("The numbet is odd")

if 1<=number <=50:
    print("It's a small Number.")
elif 51<=number <=100:
    print("It's a mediam Number.")
elif number > 100:
    print("It's a Large Number:")
else:
    print("The number is not in any specified range.")