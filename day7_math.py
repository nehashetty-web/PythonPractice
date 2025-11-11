import random
import string
password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
print(password)


'''Find the area and circumference of a circle using math.pi.
Simulate a dice roll using random.randint(1, 6).
Create a random password generator using:'''

import math

# Take radius as input
radius = float(input("Enter the radius of the circle: "))

# Calculate area and circumference
area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius

# Display results
print(f"Area of circle: {area:.2f}")
print(f"Circumference of circle: {circumference:.2f}")


import random

print("🎲 Rolling the dice...")
dice = random.randint(1, 6)
print("You got:", dice)
