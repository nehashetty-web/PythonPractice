'''List: Add, remove, and update elements in a list.
Tuple: Find length, count of an element, and index of an element in a tuple.
Set: Add and remove elements from a set.
Set Operations: Find union, intersection, and difference of two sets'''
"solutions"
fruits=["apple","orange","kiwi"]
fruits.append("chikko")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits[1]="grapes"

num=(1,2,3,4,8,9,5,4,4)
print(len(num))
count=num.count(4)
print(count)
index=num.index(8)
print(index)
