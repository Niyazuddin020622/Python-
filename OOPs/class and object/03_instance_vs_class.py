class Employee():
    language = "Python" # This is a class attributes
    salary = 120

niyazu = Employee() # This is an object

niyazu.language = "JavaScript" # This is an instance attributes

print(f"Your Language {niyazu.language}, and salary: {niyazu.salary}")