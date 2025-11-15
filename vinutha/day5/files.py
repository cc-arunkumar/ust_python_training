import os

# Example of opening a file in write mode and writing content
# file = open("hello_file.txt", "w")  
# file.write("Hello World\n")
# file.write("welcome to file handling in python\n")  
# file.write("The line end\n")
# print(file)
# file.close()

# Using 'with' ensures the file is automatically closed after writing
# with open("hello_file.txt","w") as file:
#     file.write("Hello World\n")
#     file.write("welcome to file handling in python\n")
#     file.write("The line end\n")

# Reading the entire file content
# with open("hello_file.txt","r") as file:
#     content=file.read()
#     print(content)

# Checking if file exists before reading
# if os.path.exists("hello_file.txt"):
#     with open("hello_file.txt","r")as file:
#         content=file.read()
#         print(content)
# else:
#     print("The file not found")

# Removing a file (note: typo in filename "hello_file.text" should be "hello_file.txt")
# os.remove("hello_file.txt")

# Reading file line by line
# with open("hello_file.txt","r") as file:
#     for line in file:
#         print(line.strip())
# print("=== line by line reading===")

# Read all lines into a list
with open("hello_file.txt", "r") as file:
    lines = file.readlines()

# Add line numbers to each line and overwrite the file
line_number = 1
with open("hello_file.txt", "w") as file:
    for line in lines:
        file.write(f"{line_number}. {line}")  # Prefix line with its number
        line_number += 1
