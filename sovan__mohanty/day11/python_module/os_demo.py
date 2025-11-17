import os

print("current_directory_path=",os.getcwd())
print("List directory ",os.listdir())

new_dir="sub_dir"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print("New directory created")
else:
    print("New directory failed to create")
    
print("List directory ",os.listdir())

final_file="final_file.txt"
if not os.path.exists("dummy_file.txt"):
    os.mkdir("dummy_file.txt")
    print("New directory created")
else:
    os.rename("dummy_file.txt",final_file)
    print("New directory failed to create")


