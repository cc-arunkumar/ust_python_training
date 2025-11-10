import os

#write operation
with open("file01.txt","w") as f:
    f.write("Hii\n")
    f.write("vanakam\n")
    f.write("this is shyams file\n")
    
#read operation
# with open("file01.txt","r") as f:
#     content=f.read()
#     print(content)
#     f.close()

#accessin if that file exist
# if os.path.exists("file1.txt"):
#     with open("file1.txt","r") as f:
#         content=f.read()
#         print(content)
        
# else:
#     print("File not found")

#Removing a file
# os.remove("file01.txt")

with open("file01.txt","r") as f:
    x=1
    for line in f:
        print("Line",x,":",line.strip())
        x+=1
        
with open("file01.txt","a") as f:
    f.write("last second\n")
    f.write("Last Line\n")