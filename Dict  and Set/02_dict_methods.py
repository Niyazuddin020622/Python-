marks = {
    "Niyazuddin":100,
    "rani":98,
    "Meraj":87
}

print(marks.items())

# key method

print(marks.keys())
# value
print(marks.values())

# Update values
marks.update({"Niyazuddin":99,"Renuka":88})
print(marks)

# update key 
marks["Ansari"] = marks.pop("Niyazuddin")
print(marks)

print(marks.get("rani")) # print none jab dict me key nhi rahe or dusra key likhe to erro nhi none dega
print(marks["rani"]) # jab dict me key ho to success agar nhi ho to error dega ye 

# POP

name =marks.pop("rani") # pop remove karta hai key insert karna parta hai remove karane ke liye jo rani key hai 
print(name)
print(marks)

# popitem

my_dict = marks.popitem() # popitems last ke key or values output deta hai
print(my_dict)

keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, "default")
print(new_dict)  # Output: {'name': 'default', 'age': 'default', 'city': 'default'}
