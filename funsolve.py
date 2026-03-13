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