'''Create a class with two instance variables using __init__(). Create two objects and
 change one object’s variable. Print both.
Create a class with one static variable and one instance variable.
 Create two objects and change the static variable. Print the values.
Create a class with one instance variable. Create two objects with different values.
 Change one object’s value and print both.
Create a class with one static variable and one instance variable. Create two objects
 and modify the static variable. Print values for both objects.
Create a class using __init__() with two instance variables. Create three objects and 
change one variable of one object. Print all object values.'''
"solutions"
class Dog:
    colour="brown"
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

d1 = Dog("Tommy", "Brown")
d2 = Dog("Rocky", "Black")

# Change variable of d1
d1.colour = "White"
Dog.colour = "pink"
print(d1.name, d1.colour)
print(d2.name, d2.colour)
print(Dog.colour)