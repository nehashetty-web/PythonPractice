'''
1. Write a Python program to store your name, age, and marks in variables and display them.
2. Write a program to take two numbers as input from the user and print their sum, difference, product, and quotient.
3. Write a Python program to check the data type of a given variable.
4. Write a program to check whether a given number is positive, negative, or zero using `if–else`.
5. Write a program to display grades based on marks using `if–elif–else`.
6. Write a Python program to print all even numbers from 1 to 50 using a `for` loop.
7. Write a program to print numbers from 1 to 10, skipping 5 and stopping the loop when the number is 7.
8. Write a Python program demonstrating the use of `break`, `continue`, and `pass`.
9. Write a program to print a star pattern using nested loops.
10. Write a Python program to count the numbers between 1 and 100 that are divisible by both 3 and 5.
'''

#SOLUTIONS
name = input("enter your name ")
age=int(input("enter your age"))
marks=int(input("enter your marks"))
print("Name:", name)
print("Age:", age)
print("Marks:", marks)

num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
add=num1+num2
print(add)
sub=num1-num2
print(sub)
mul=num1*num2
print(mul)
quot=num1/num2
print(quot)

a=10
print(type(a))
