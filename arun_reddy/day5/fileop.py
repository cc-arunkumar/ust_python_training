# writing to the file,if file doesnot exit it creates a new one 
file=open("example.txt","w")
file.write("Hello world")
file.write(" File handling Concepts.......")
#reading from teh file 
file=open("example.txt","r")
print(file.read())
# closing the file 
file.close()



file=open("D:/ust_python_training/arun_reddy/day5/report.txt","r")
content=file.read()
print(type(content))    
f=open("test.txt","w")
f.write(content)
print(content)
f.close()

print("using the readlines - CORRECTED")
# Better way: use 'with' statement (auto closes file)
with open("D:/ust_python_training/arun_reddy/test.txt", "r") as f2:
    readl = f2.readlines()
    f2.seek(0)
    for line in readl:
        print(line.strip())  # strip() removes extra newline from readlines()
# File automatically closed when exiting 'with' block
