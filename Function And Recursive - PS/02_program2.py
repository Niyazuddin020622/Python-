def greater(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = int(input("Enter your first numebr: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third numebr: "))

print(f"Greater Number is: {greater(a,b,c)}")