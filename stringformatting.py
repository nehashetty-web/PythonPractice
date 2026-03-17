name="neha"
age= 19
"f string"
print(f"my name is {name}")
"formart"
print("my name is {}".format(name))
"% operator"
print("my name is %s" %name)

"SOLVING"
"• Practice: vowel count, digit extraction, palindrome substring"
"VOWEL COUNT"
s="college"
count=0
for  ch in s:
    if ch in "aeiouAEIOU":
        count=count+1
print(count)

"digit extraction"
s="neha2007"
digits=""
for ch in s:
    if ch.isdigit():
        digits=digits+ch
print(digits)

"palindrome"
s="madam"
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub=s[i:j]
    if sub==sub[::-1] and len(sub) > 1:
        print(sub)


s="gurucharan"
print(s[0]) 
print(s[-1])
print(s[0:5])

s="python"
print(s[1:4])


s="PYTHON PROGRAMMING"
print(s.lower())

s="python programming"
print(s.upper())

s="AM LEARNING PYTHON "
print(s.split()) 

def char_frequency(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    print(freq)
char_frequency("lovely") 

def check_anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        print("its anagram")
    else:
        print("not anagram")
check_anagram("race","care")
