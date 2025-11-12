try:
    f = open("notes.txt", "r")
    content = f.read()
    print(content)
except Exception as e:
    print("Something went wrong:", e)
else:
    print("File read successfully!")
finally:
    f.close()
