n = int(input("Enter a number: "))

table = [n*i for i in range(1,11)]
with open("ADVANCE PYTHON - PS/table.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")