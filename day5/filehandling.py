#file handling

import os

with open("example.txt","w") as file:
    file.write("welcome\n")
    file.write("file handling\n")
    file.write("the end\n")
with open("example.txt","r") as file:
    content=file.read()
    print(content)

if os.path.exists("example.txt"):
    with open("example.txt","r") as file:
        content=file.read()
        print (content)
else:
    print("reading completed")
print("writing completed")

with open("example.txt","r") as file:
    for line in file:
        print(line.strip())
print("=== line by line ====")
with open("example.txt","r") as file:
    lines=file.readlines()
line_num=1
with open("example.txt","w") as file:
    for line in lines:
        file.write(f"{line_num}.{line}")
        line_num += 1

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

