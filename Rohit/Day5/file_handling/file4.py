import os
# if os.path.exists("t1.txt"):
    
#     with open("t1.txt", "w") as file:
#         file.write("Hello from the file side\n")
#         file.write("Hello from the file side\n")
#         file.write("welcome to file handling in python using with\n")


i=1
word= "file"
with open("t1.txt","r") as file:
    for line in file:
        if word in line:
            print(f"word found {word} at line: {i}")
        # print(f"line: {i} ",line.strip())
        i+=1



with open("t1.txt", "a") as file:
    file.write("Appending line 1\n")
    file.write("Appending line 2\n")
    file.write("Appending line 3\n")