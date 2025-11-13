 # Safe file handling using 'with'
with open("example.txt", "w") as f:
    f.write("This is safely written using 'with' statement.\n")

# Reading file
with open("example.txt", "r") as f:
    print(f.read())

# Try r+ mode
with open("example.txt", "r+") as f:
    print(f.read())
    f.write("\nAdding new line using r+ mode.")

# Handle file not found
try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("⚠️ File not found. Check the name again.")
   
