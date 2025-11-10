# file =open("file.txt","r")
# read =file.readlines()
# print(read)
# file.close()

#File reader writer

# import os
# if os.path.exists("file1.txt"):
#     with open("file1.txt","w") as file:
#         file.write("------Hello------\n")
#         file.write("Hello everyone")
# else:
#     print("File doesnot exit")

# if os.path.exists("file1.txt"):  
#     with open("file1.txt", "r") as file:
#         content=file.read()
#         print(content)
# else:
#     print("File cannot be read")
# print("Reading compleded")


import os
if os.path.exists("file21.txt"):
    with open("file21.txt","w") as file:
        file.write("Hello ")
        file.write("Sohan")
else:
    print("file doesnot exixts")

if os.path.exists("file21.txt"):
    with open("file21.txt") as file:
        content=file.read()
        print(content)
else:
    print("File is not available")
    


        
