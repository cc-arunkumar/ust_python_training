import os

with open("file1.txt", "w") as file:
    file.write("I am working in UST\n")
    file.write("I am having training\n")

with open("file1.txt", "r") as file:
    content = file.read()
    print(content)

if os.path.exists("file1.txt"):
    with open("file1.txt", "r") as file:
        content = file.read()
        print("File content (after checking existence):")
        print(content)
else:
    print("The file does not exist")
    

