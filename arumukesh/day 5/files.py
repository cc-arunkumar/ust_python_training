import os
with open("file.txt", "w") as file:
    file.write("Hello, World!\n") 
    file .write("This is a sample file.\n")

if os.path.exists("file.txt"):
    with open("file.txt", "r") as file:
        content = file.read()
        print(content)
else:
    print("The file does not exist.")

os.remove("file.txt")
