import os 

print("Current directiory path = ",os.listdir())
print("Current directiory path = ",os.getcwd())

new_dir ="Sub-dir"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
else:
    print("Cannot be created")
    

print("Current directiory path = ",os.listdir())

# #Output
# Current directiory path =  ['.git', '.gitignore', 'data', 'dummy_file', 'dummy_file.txt', 'employees.txt', 'final_file.txt', 'README.md', 'sohan-kumar-rout', 'Sub-dir']
# Current directiory path =  C:\Users\Administrator\Desktop\PTraining\ust_python_training
# Cannot be created
# Current directiory path =  ['.git', '.gitignore', 'data', 'dummy_file', 'dummy_file.txt', 'employees.txt', 'final_file.txt', 'README.md', 'sohan-kumar-rout', 'Sub-dir']

file1 = "final_file.txt"
if not os.path.exists("dummy_file.txt"):
    os.mkdir("dummy_file.txt")
    print("Created sucessfully")
else:
    os.rename("dummy_file.txt",file1)
    

