''''practise questions
Create a tuple with 5 numbers and print its first and last element.
Try changing a tuple element and note the error.
Use count() and index() methods.
Create two sets of numbers and find their union, intersection, and difference.
Convert a list with duplicates into a set'''
tuple=(1,2,4,6,6,5,7,6)
print(tuple[0],tuple[-1])
print(tuple.count(6))
print(tuple.index(2))

# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
print("Union:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))

# Difference
print("Difference (set1 - set2):", set1.difference(set2))
print("Difference (set2 - set1):", set2.difference(set1))

list=[1,2,3,3,4,5,7,7,8]
set=set(list)
print(set)