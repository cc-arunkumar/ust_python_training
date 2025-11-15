#file handling
# This program demonstrates basic file handling operations in Python using the file example.txt.
# It first writes three lines (welcome, file handling, the end) into the file.
# Then it reads the entire file content and prints it
import os

# Write some initial content into the file
with open("example.txt","w") as file:
    file.write("welcome\n")
    file.write("file handling\n")
    file.write("the end\n")

# Read and display the file content
with open("example.txt","r") as file:
    content = file.read()
    print(content)

# Check if file exists before reading again
if os.path.exists("example.txt"):
    with open("example.txt","r") as file:
        content = file.read()
        print(content)
else:
    print("reading completed")
print("writing completed")

# Read file line by line
with open("example.txt","r") as file:
    for line in file:
        print(line.strip())

print("=== line by line ====")

# Read all lines into a list
with open("example.txt","r") as file:
    lines = file.readlines()

# Rewrite file with line numbers
line_num = 1
with open("example.txt","w") as file:
    for line in lines:
        file.write(f"{line_num}.{line}")
        line_num += 1

# Append new lines at the end of the file
with open("example.txt","a") as file:
    file.write("appending new line\n")
    file.write("appending line 2\n")

print("=== appending completed ===")

# welcome      
# file handling
# the end      

# welcome
# file handling    
# the end

# writing completed
# welcome
# file handling
# the end
# === line by line ====
# === appending completed ===