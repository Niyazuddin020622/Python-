def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n * i}")
table(6)



def usertable(n):
    for i in range(1,11):
         print(f"{n} X {i} = {n * i}")
n = int(input("Enter a number: "))
usertable(n)



def usertable(n):
    for i in range(1,11):
         print(f"{n} X {i} = {n * i}")

for _ in range(4):
    n = int(input("Enter a number: "))
    usertable(n)

