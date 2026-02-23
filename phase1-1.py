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
def analyze_text(s):
    vowels = 0
    consonants = 0
    total_chars = 0
    
    for ch in s:
        if ch != " ":
            total_chars += 1
            
        if ch.lower() in "aeiou":
            vowels += 1
            
        elif ch.isalpha():
            consonants += 1
def count_vowels(s):
   count=0
   for ch in s: 
      if ch.lower() in "aeiou":
         count +=1
   return count
def find_max(lst):
   max=lst[0]
   if num > max :
      max += 1
   else:
        return max
def count_even(lst):
   count=0
   for num in list:
      if num%2==0:
         count += 1
   return count   
def sum_positive(lst):
   count=0
   for num in lst:
      if num>0:
         count +=1
   return count    
def contains_negative(lst):
   for num in lst:
      if num <0:
         return True
      else:
         return False
class car:
   def __init__(self,brand,speed):
      self.brand=brand
      self.speed=speed
c1=car("bmw",60)
c2=car("lambo",90)

print(c1.brand)
print(c2.speed)