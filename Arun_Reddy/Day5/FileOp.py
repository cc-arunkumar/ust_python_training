# writing to the file,if file doesnot exit it creates a new one 
file=open("example.txt","w")
file.write("Hello world")
file.write(" File handling Concepts.......")
#reading from teh file 
file=open("example.txt","r")
print(file.read())
#closing the file 
file.close()