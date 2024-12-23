s = {1,2,4,5,6,"Nitya"}

print(s, type(s))

s.add(566) # add items
print(s,type(s))

# copy 
my_set = {1, 2, 3}
new_set = my_set.copy()
print(new_set)  # Output: {1, 2, 3}

#   4. difference(other_set)
# Returns a set containing the difference of two sets (elements in the first set but not in the second)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.difference(set2))  # Output: {1, 2}

s.remove(1)
print(s)

s.clear()
print(s)

s = set1.union(set2)
print(s)

s = set1.intersection(set2)
print(s)