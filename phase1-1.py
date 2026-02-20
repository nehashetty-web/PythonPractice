''' Set 1 – Very Basic Functions (No Tricks)
Write a function that returns square of a number.
Write a function that prints numbers from 1 to n.
Write a function that returns the largest of two numbers.
Write a function that checks if a number is positive, negative, or zero.
Write a function that returns the length of a string (without using len()).'''
def square(n):
 return n**2
n=int(input("enter number"))
print(square(n))
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)
num = int(input("Enter number: "))
print_numbers(num)
def largest(num1,num2):
 
   if num1>num2:
    return(num1)
   elif num2>num1:
    return(num2)

 
num1=int(input("Value1"))
num2=int(input("value2"))
print(largest(num))