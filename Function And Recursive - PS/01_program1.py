def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter your number: "))
print(f"The factorial of this number is: {factorial(n)}")