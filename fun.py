def returnValueFunction(n):
    c=n*2
    return c

returnValueFunction(6)

#Write the helloFunction below. It should have one statement
#print("Hello")
#code here
def helloFunction():
    print("Hello")
helloFunction()
def power(base,exponent=2):
    print(base**exponent)
power(2)
power(2,3)
def employee(name,salary):
    print(name,salary)
employee(salary=30000,name="varsh")
def area(length,breadth):
    print(length*breadth)
area(6,8)
cube=lambda x:x**3
print(cube(6))
def show_number():
    n=50
    print(n)
show_number()
message="hello"
def greetings():
    print(message)
greetings()
company="techcrop"

def checking(a,b):
    try:
        result=a/b
        print(result)
    except:
        print("unable to divide")
checking(100,20)
checking(100,0)

