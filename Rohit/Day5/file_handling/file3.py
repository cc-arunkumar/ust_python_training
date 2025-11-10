import os
with open("t1.txt", "w") as file:
    file.write("Hello from the file side\n")
    file.write("Hello from the file side\n")
    file.write("welcome to file handling in python using with\n")
    
    
with open("t1.txt", "r") as file:
    content = file.read()
    print(content)
    

if os.path.exists("t1.txt"):
    
    with open("t1.txt", "w") as file:
        file.write("Hello from the file side\n")
        file.write("Hello from the file side\n")
        file.write("welcome to file handling in python using with\n")
else:
    print("The file does not existed")
    
# os.remove("t1.txt")


with open("t1.txt","r") as file:
    for line in file:
        print(line.strip())
        
print("==== line by line Reading completed======")