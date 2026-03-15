def factorial(n):
    result=1
    for i in range(1,n+1):
        result= result*i
    print(result)
factorial(6)

def reverse(n):
    reverse=0
    while n>0:
        digit= n %10 
        reverse= reverse *10+digit
        n= n//10
    print(reverse)
    if n == reverse:
       print ("is palindrome")
    else:
        print("not palidrome")
reverse(224422)
def count(n):
    count=0
    while n>0:
        n=n//10
        count=count+1
    print(count)
count(7330776660)

arr=[5,10,15,20]
for num in arr:
    print(num)

def linear_serach(arr,target):
    for i in range (len(arr)):
        if arr[i]==target:
            print("found at index",i)
            return
    print("not found")
arr = [6, 2, 9, 15, 3] 
linear_serach(arr,100)
def reverse_array(arr):
    left=0
    right=len(arr)-1
    while left < right :
        arr[left],arr[right]=arr[right],arr[left]
        left=left+1
        right=right-1
    arr = [5, 8, 2, 9, 1]

reverse_array(arr)
print(arr)
def print_demo(n):
    if n==0:
        return
    print(n)
    print_demo(n-1)
print_demo(5)

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(6))

def sum(n):
    if n==0:
        return 1
    return n+sum(n-1)
print(sum(6))

def fibonnaci(n):
    if n==0: 
        return 0
    if n==1:
        return 1
    return fibonnaci(n-1)+fibonnaci(n-2)
print(fibonnaci(34)) 

def reverse(s):
    if s=="": 
        return s
    return reverse (s[1:])+s[0]
print(reverse("hello"))
