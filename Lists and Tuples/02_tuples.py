a = (1,24,65,"Niyazuddin Ansari", False)

print(a)

# 1. count()
no = a.count(24)
print(no)

# 2. index()

index = a.index(24)
print(index)

# 3. Tuple Concatenation

number1 = (1,2,3,5)
number2 = (3,4,5,6)

number3 = number1+number2
print(number3)

# 4. Tuple Repetition
my_tuple = (1,2,4)

result = my_tuple*2
print(result)

# 5. Tuple Membership Test

print(1 in number1)
print(2,not number1)

# 6. Tuple Slicing
print(number1[0:2])

# 7. Tuple Length
print(len(number1))

# 8. Tuple Conversion

my_tuple = tuple(number1)
print(my_tuple)

# 9. Tuple Iteration

for item in my_tuple:
    print(item)

# 10. Tuple Unpacking
my_tuple = (1,2,3)
a,b,c = my_tuple
print(a,b,c)

