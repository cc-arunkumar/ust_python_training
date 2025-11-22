import os
# filw writing using the context manager
with open("example.txt","w") as file:
    file.write("=======file wrintg====== \n")
    file.write("using the context manager \n")
    file.write("handling file ops")


print("Writing is completed")
#file reading using the context manager 
if os.path.exists("example.txt"):
    with open("example.txt","r") as file:
        content=file.read()
        print(content)
else:
    print("File do not exist")


print("Reaing completed")

# using the strip() function 
with open("example.txt","r") as file:
    # i=1
    # for line in file:
    #     print(f"Line-{i} {line.strip()}")
    #     i=i+1
    for ind,line in enumerate(file):
        print(f"Line-{ind+1} {line.strip()}")
        
        # removes the new line charcetrs so it doesnt give thebuffer space 
    

with open("example.txt","a") as file:
    file.write("\n Helooo------")
    
with open("example.txt","r") as file:
    for line in file:
        print(line.strip())



str="handling file ops"

with open("example.txt","r") as file:
    for line in file:
        if line.strip()==str:
            print("found")
os.remove("example.txt")
