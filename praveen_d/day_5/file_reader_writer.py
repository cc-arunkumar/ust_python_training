# Filw writing using context manager

with open("file01.txt","w") as file:
    file.write("Started the file handling with with\n")
    file.write("ok done\n")
    file.write("Writting completes here\n")

# with open("file01.txt","r") as file:
#     context=file.read()
#     print(context)


with open("file01.txt","r") as file:
    i=1
    for line in file:
        print(f"{i}.{line.strip()}")
        i+=1