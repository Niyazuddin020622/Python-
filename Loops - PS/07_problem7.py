n = int(input("Enter your number: "))

if n < 0:
    print("factorial is not defined for negative numbers: ")
elif n == 0 or n == 1:
    print(f"The factorial of {n} is: 1")
else:
    result = 1
    for i in range (2,n+1):
        result *=i
    print(f"The factorial of {n} is: {result}")