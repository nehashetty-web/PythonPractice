'''Write a function that takes two numbers as arguments and returns their product.
 Call the function and print the result.
Write a function greet_user that takes a name as a parameter and a default argument 
message="Welcome" and prints the greeting. Call the function once with both arguments 
and once with only the name.
Write a function student_details that takes name, age, and course as parameters. 
Call the function using keyword arguments in a different order and print the details.'''
"solutions"
def mul(a,b):
    return a*b
result=mul(3,4)
print(result)


def greet_user(name, message="Welcome"):
    print(message, name)
greet_user("Neha", "Hello")
greet_user("Neha")

def student_details(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
student_details(course="Python", name="Neha", age=21)

