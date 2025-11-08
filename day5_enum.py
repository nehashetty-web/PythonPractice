'''Practice Tasks:
Print numbers 1–10 using range().
Loop over a list using enumerate() and print index + value.
Combine two lists (names + marks) using zip() and print pairs.'''

for i in range(1,11):
    print(i)

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)


names=['neha','uday','varsh']
marks=[90,78,90]
data=zip(names,marks)
print(list(data))

