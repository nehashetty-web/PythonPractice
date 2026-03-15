#Practice Tasks:
#create a list and print first 3 elements
#Add and remove an element using append(), insert(), and pop().
#Sort a list of numbers and reverse it.

#1
fruits=[ "apple","orange","kiwi","grapes","banana"]
print(fruits[:3])
#2
fruits.append("guava")
print(fruits)
fruits.insert(2,"cherry")
print(fruits)
fruits.pop()
print(fruits)
#3
nums=[9,8,3,7,3,0,2]
nums.sort()
print(nums)
nums.reverse()
print(nums)