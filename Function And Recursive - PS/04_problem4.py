def evenodd(n):
    if(n%2==0):
        print(f"{n} is even number")
       

    else:
        print(f"{n} is odd number")
       
n = int(input("Enter your number: "))
evenodd(n)


# For Loop using check code even or odd

def evenodd(n):
    if(n%2==0):
        print(f"{n} is even number")
       

    else:
        print(f"{n} is odd number")
       
for _ in range(4):
    n = int(input("Enter your number: "))
    evenodd(n)
