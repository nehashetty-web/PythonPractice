#functions
a=int(input("enter n1"))
b=int(input("enter n2"))
def large(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        print("both equal")
print(large(a,b))
#lists
nums = [10, 20, 30, 40, 50]
nums.append(60)
nums.pop(1)
print(nums)
#dict
student={"name":"neha","age":19}
student["branch"]="CSD"
print(student.keys())
print(student.values())
#oops
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("Neha",19)
print(s1.name)
print(s1.age)

with open("file.txt","r")as file:
    data=file.read()
with open("file.txt","w")as file:
    file.write("hello neha")
print(data)

num1=int(input("n1"))
num2=int(input("n2"))
def divison(num1,num2):
    try:
        print(num1/num2)
    except:
        print("cant divide by zero")
divison(num1,num2)

s="banana"
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)
#python recap
a=input("enter string: ").lower()
for ch in a:
    if ch in "aeiou":
        print("string is vowel")
    else:
        print("string is consonant")
ch=input("enter input")
if ch.isalpha:
    print("alphabet")
else:
    print("not alphabet")
ch=input("enter ch:")
print(ord(ch))
num = int(input("Enter an integer: "))
count = 0

while num != 0:
    count += 1
    num //= 10

print(count)


   
