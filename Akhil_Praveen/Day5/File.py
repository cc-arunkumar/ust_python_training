import os
# file = open("file01.txt","w")
# file.write("Hello\n")
# file.write("this is second line\n")
# file.write("this 3rd line\n")
# file.close()
# file = open("file01.txt","r")
# print(file.read())
# file.close()
# file = open("file01.txt","w")
# file.write("Hello\n")
# file.write("this is ")
# file.close()
# file = open("...\\link.txt","r")
# print(file.read())
# file.close()

# file writing using context manager
with open("file01.txt","w") as file:
    file.write("Hello\n")
    file.write("this is second line\n")
    file.write("this 3rd line\n")

# file reading using context manager
# with open("file1.txt","r") as file:
#     print(file.read())
# os.remove("file01.txt")
# if os.path.exists("file01.txt"):
#     with open("file01.txt","r") as file:
#         print(file.read())
# else:
#     print("file does not exist")
with open("file01.txt","a") as file:
    file.write("appending 1 line\n")
    file.write("appending 2 line\n")

with open("file01.txt","r") as file:
    # i=1
    line = file.readlines()
    for i in range(len(line)):
        print(f"line {i}:",line[i].strip())
        

        
with open("file01.txt","r") as file:
    line = file.readlines()
    for i in range(len(line)):
        if "Hello" in line[i]:
            print(f"line {line[i].strip()} is present")
with open("file01.txt","r") as file:
    line = file.readlines()
    print(line)