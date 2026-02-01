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