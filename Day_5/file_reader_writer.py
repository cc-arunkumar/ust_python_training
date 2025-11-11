import os


with open("file.txt","w") as file:
    
    
    file.write("****Welcome****\n")
    file.write("This is an example for file reader\n")
    file.write("----> The END <----\n")
print("==== Writing Completed====")

    
# with open("file1.txt","r") as file:
#     content=file.read()
#     print(content)
    
# if os.path.exists("file.txt"):
#     with open("file.txt","r") as file:
#         content=file.read()
#         print(content)
# else:
#     print("File Not found")
    
# print("Reading Complted")

# os.remove("file.txt")
# print("===File Deleted Successfully===")

# if os.path.exists("file.txt"):
#     with open("file.txt","r") as file:
#         content=file.read()
#         print(content)
# else:
#     print("File Not found")

# with open("file.txt","r") as file:
#     i=1
#     for line in file:
#         print(f"Line {i}:{line.strip()}")
#         i+=1
        
# print("====Line by Line Reading Completed====")


with open("file.txt","a") as file:
    file.write("Appending new line 1\n")
    file.write("Appending new Line 2\n")

print("=== Appending Completed===")

target="appending"
flag=False
if os.path.exists("file.txt"):
    with open("file.txt","r") as file:
        content=file.read()
        print(content)
    
    for line in content:
        if target.lower() in line.lower():
            print(f"target found:{line.strip()}")
            flag=True
    if not flag:
        print("target not found")        
        
    
else:
    print("File Not found")
    
print("Reading Complted")