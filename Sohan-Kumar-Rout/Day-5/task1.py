import os
if os.path.exists("sohan.txt"):
    with open("sohan.txt", "w") as file:
        file.write("This is my file\n")
        file.write("All the employee data are here \n")
else:
    print("file doesnot exists")

if os.path.exists("sohan.txt"):
    with open("sohan.txt", "r") as file:
        read = file.read()
        print(read)
else:
    print("File is not available")
    