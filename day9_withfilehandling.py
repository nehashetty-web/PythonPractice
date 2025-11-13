# Create and write to file
f = open("notes.txt", "w")
f.write("Hey, this is Neha’s first file!\nLearning Python is fun.\n")
f.close()

# Read and print content
f = open("notes.txt", "r")
print(f.read())
f.close()

# Append new lines
f = open("notes.txt", "a")
f.write("Appending new line to existing file.\n")
f.close()

# Count words, lines, and characters
with open("notes.txt", "r") as f:
    data = f.read()
    print("Words:", len(data.split()))
    print("Lines:", data.count("\n") + 1)
    print("Characters:", len(data))
# Handle division safely
try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    print(a / b)
except ZeroDivisionError:
    print("You can’t divide by zero!")
except ValueError:
    print("Please enter valid numbers!")
finally:
    print("Program completed safely.")

# File handling with exception
try:
    with open("notes.txt", "r") as f:
        print(f.read())
except Exception as e:
    print("Error:", e)
else:
    print("File read successfully!")
