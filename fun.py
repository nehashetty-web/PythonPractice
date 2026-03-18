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
def employee_info(name,salary):
    bonus=2000
    total_salary=salary+bonus
    tax=lambda salary: salary//10
    print(company)
    print(employee_info("neha"))
    print(total_salary)
    print(tax)
employee_info("neha",890990)