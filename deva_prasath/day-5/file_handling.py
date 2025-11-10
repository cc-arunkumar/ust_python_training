import os
file=open("dev.txt",'w')
file.write("Hello, Dev\n")
file.write("This is file handling\n")

# os.remove("dev1.txt")
# print("File deleted")
# if os.path.exists("dev1.txt"):
#     with open("dev1.txt",'r') as f:
#         content=f.read()
#         print(content)
# else:
#     print("The file does not exist.")

with open("dev.txt",'r') as file:
    i=1
    for line in file:
        print(f"Line {i}:",line.strip())
        i+=1

with open("dev.txt",'a') as file:
    file.write("Pluribussss\n")