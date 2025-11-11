#File writing/reading with context manager

with open("file2.txt","w") as file1:
    file1.write("******File Handling******\n")
    file1.write("Welcome to file handling class\n")
with open("file2.txt","r") as file:
    content = file.read()
    print(content)

# #Sample Output
# # ******File Handling******
# # Welcome to file handling class


import os
if os.path.exists("file1.txt"):
    with open ("file1.txt","r") as file:
        content = file.read()
        print(content)
else:
    print("File does not exist")
os.remove("file1.txt")
print("File deleted")

#Sample Execution
# Welcome to File Handling Class
# End Class
# File deleted


#Print data line by line
with open ("file2.txt","r") as file:
    c=0
    for line in file:
        c += 1
        print("Line: ",c)
        print(line.strip())
#Sample output
# Line:  1
# ******File Handling******
# Line:  2
# Welcome to file handling class


#Append into the file
with open("file2.txt","a") as file:
    file.write("New line appended\n")
    file.write("Have a nice day\n")
    


    