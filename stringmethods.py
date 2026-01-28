# 1. split() – break sentence into words
sentence = "Python is very easy"
words = sentence.split()
print("Split:", words)

# 2. join() – join list into a sentence
joined_sentence = " ".join(words)
print("Join:", joined_sentence)

# 3. isalpha() and isdigit()
name = "Neha"
age = "21"
print("Is name alphabet only?", name.isalpha())
print("Is age digit only?", age.isdigit())

# 4. strip() – remove extra spaces
user_input = "   Hello Python   "
clean_input = user_input.strip()
print("After strip:", clean_input)

# 5. replace() – change word
text = "I like Java"
new_text = text.replace("Java", "Python")
print("After replace:", new_text)
