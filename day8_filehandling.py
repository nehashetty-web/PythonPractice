file=open("data.txt","w")
file.write("hello neha")
file.close()

file=open("data.txt","r")
print(file.read())
file.close()

file=open("data.txt","a")
file.write("\n welcome")
file.close()