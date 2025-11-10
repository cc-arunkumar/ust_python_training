import os

# file = open("hello_file.txt", "w")  
# file.write("Hello World\n")
# file.write("welcome to file handling in python\n")  
# file.write("The line end\n")
# print(file)
# file.close()

# with open("hello_file.txt","w") as file:
#     file.write("Hello World\n")
#     file.write("welcome to file handling in python\n")
#     file.write("The line end\n")


# with open("hello_file.txt","r") as file:
#     content=file.read()
#     print(content)


# if os.path.exists("hello_file.txt"):
#     with open("hello_file.txt","r")as file:
#         content=file.read()
#         print(content)
# else:
#     print("The file not found")

# os.remove("hello_file.text")  to remove the fiel

# with open("hello_file.txt","r") as file:
#     for line in file:
#         print(line.strip())
# print("=== line by line reading===")

with open("hello_file.txt", "r") as file:
    lines = file.readlines()

line_number = 1
with open("hello_file.txt", "w") as file:
    for line in lines:
        file.write(f"{line_number}. {line}")
        line_number += 1
        
