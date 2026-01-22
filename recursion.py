def outer():
    def inner():
        print("I am inner")
    inner()

outer()

x = 5

def outer():
    x = 10
    def inner():
        print(x)
    inner()

outer()
n=int(input("enter num:"))
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(n)
print(result)