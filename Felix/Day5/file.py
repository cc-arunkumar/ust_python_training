# File writing

file = open("hello.txt","w")

file.write("welcome\n")
file.write("to the world of python\n")
file.write("thnku\n")

file.close()

# File writing

file = open("hello.txt","r")

content = file.read()
print(content)

file.close()

# with oporation

with open("hello.txt","w") as file:
    file.write("=====welcome=====\n")
    file.write("to the world of python\n")
    file.write("===thnku===\n")

import os
if os.path.exists("hello.txt"):
    with open("hello.txt","r") as file:
        content = file.read()
        print(content)
else:
    print("File does not exists")
    
        
with open("hello.txt","a") as file:
    file.write("hello\n")
    file.write("i am Felix")
    

with open("hello.txt","r") as file:
    i=1
    for line in file:
        print(f"Line {i}: {line.strip()}")
        i += 1

