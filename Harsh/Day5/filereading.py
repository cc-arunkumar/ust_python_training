# import os
# if os.path.exists("file1.txt"):
#     with open("file1.txt","r") as file:
#         content=file.read()
#         print(content)
# else:
#     print("does not exist")

# # os.remove("file1.txt")

with open("file1.txt","r") as file:
    i=1
    for line in file:
        print("Line ",i,":",line.strip())
        i+=1
        
