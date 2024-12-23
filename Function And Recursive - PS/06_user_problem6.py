def rem(l, word):
    n = []
    for item in l:
        n.append(item.strip(word))  # Strip only from the start and end of the string
    return n

# Collect 4 names from the user
names = []
for _ in range(4):
    name = input("Enter your name: ")
    names.append(name)

# Remove "an" from the start and end of the names
result = rem(names, "an")
print(result)
