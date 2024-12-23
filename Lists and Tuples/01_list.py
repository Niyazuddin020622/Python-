#1. How to create a list in Python?

fruits = ["apple","banana","grapes","cherry"]  

print(fruits)

#2. How to access elements in a list?

print(fruits[1])

# How to modify an elments  in a lists

fruits[1] = "Watermelon"
print(fruits)


#4. How to append an item to a list?

fruits.append("Mango")
print(fruits)

# 5. How to remove an item from a list?

fruits.remove("Mango")
print(fruits)

# 6. How to find the length of a list?

print(len(fruits))

# 7. How to sort a list?
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)  

# 8. How to reverse a list?

numbers.reverse()
print(numbers)

# 9. How to slice a list?

print(fruits[:4])

# 10. How to concatenate two lists?

number1 = [12,34,56,32,76]
number3 = numbers+number1
print(number3)

# 11. How to check if an item exists in a list?

print("apple" in fruits)

# 12. How to iterate over a list?

for fruit in fruits:
    print(fruit)

# 13. How to copy a list?

fruits_copy = fruits.copy()
print(fruits_copy)


# 14. How to clear a list?

fruits.clear()
print(fruits)

# 15. How to find the index of an item?
fruits =["apple","banana","cherry"]
print(fruits.index("cherry"))

# pop

l1 = fruits.pop((2))
print(l1)

# insert

numbers.insert(1,100)
print(numbers)

print(type(fruits))