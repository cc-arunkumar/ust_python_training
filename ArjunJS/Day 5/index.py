import os
# file = open("file1.txt","w")
# file.write("Hi Hellooo\n")
# file.write("Bye Byee\n")
# file = open("file1.txt","r")
# print(file.read())
# file.close()
with open("file1.txt","w") as file:
    file.write("*********File Handling**********\n")
    file.write("Welcome to file handling in Python using with.\n")
    file.write("------> The END <------\n")
    file.close()


# os.remove("file1.txt")
# if os.path.isfile("file1.txt"):
#     with open("file1.txt","r") as file:
#         print(file.read())
#     file.close()
# else:
#     print("File not found!!")

if os.path.isfile("file1.txt"):
    with open("file1.txt","a") as file:
        file.write("Appending Data")
    file.close()
else:
    print("File not found!!")

x="------> The END <------"
if os.path.isfile("file1.txt"):
    with open("file1.txt","r") as file:
        ch=1
        for i in file.readlines():
            if(i.strip()==x):
                print("Found!!!")
            print(f"Line {ch} : {i.strip()}")
            ch+=1
    file.close()
else:
    print("File not found!!")

