import os
# with open("file.txt",'w') as file:
#     file.write("-------- file handling -------")
#     file.write("write to file")
    
# with open("file.txt",'r') as file:
#     content=file.read()
#     print(content)
    
    
# if os.path.exists("file.txt",):
#     with open("file.txt",'r') as file:
#         content=file.read()
#         print(content)
# else:
#     print("file not found")



# with open("file.txt",'r') as file:
#     i=1
#     for line in file:
#         print(f"line {i}: {line.strip()}")
#         i+=1


with open("file.txt",'a') as file:
    file.write("appending new line 1.\n")
    file.write("appending new line in to the file 2.\n")
print("====file appending completed===")



    

    