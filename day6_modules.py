import random

print("Random number (1–10):", random.randint(1, 10))
print("Random choice:", random.choice(["Neha", "Uday", "Varsha"]))
print("Random float:", random.random())

# Shuffle a list
names = ["Neha", "Uday", "Varsha"]
random.shuffle(names)
print("Shuffled list:", names)


import math

radius = 5
area = math.pi * math.pow(radius, 2)
print("Area of circle:", area)
print("Square root of 25:", math.sqrt(25))
print("Ceiling of 3.2:", math.ceil(3.2))
print("Floor of 3.9:", math.floor(3.9))
