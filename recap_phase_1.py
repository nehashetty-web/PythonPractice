'''Python + Logic
Write a function that returns the second largest element in a list.
Write a function using default arguments to calculate simple interest.
Write a recursive function to compute sum of digits of a number.
Given a string, count vowels, consonants, digits.
Check if two strings are anagrams.
DSA Core
Reverse an array in-place.
Find the maximum subarray sum of size k (basic sliding window).
Check balanced parentheses using stack.
Reverse a queue.
Implement linear search and return index (or -1).'''
def second_largest(arr):
    # If list has less than 2 elements, second largest doesn't exist
    if len(arr) < 2:
        return None

    largest = float('-inf')
    second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num < largest and num > second:
            second =num    
    if second == float('-inf'):
        return None

    return second
def simple_interset(r=5):
   p=int(input("principle"))
   t=int(input("time"))
   return
   (p*r*t)/100
print(simple_interset())
