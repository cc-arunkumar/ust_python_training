import os
import csv

print("current directory path=",os.getcwd())

new_dir="sub_dir"
file1="final_file.txt"
if not os.path.exists(file1):
    with open(file1,"w") as file:
        pass
else:
    
    os.rename("dummy_file.txt", file1)
    
print("current directory path=",os.listdir())

print("current directory path=",os.rename("new.txt","os_get_demo.txt"))
print("current directory path=",os.remove("os_get_demo.txt"))
print("current directory path=",os.getcwd())


target_path=os.getcwd() + '/final_dir'
new_file="final_report.txt"

if not os.path.exists(target_path):
     os.mkdir('final_dir')
else:
    print("File exists")
 
new_file_path = os.path.join(target_path,new_file)
with open(new_file_path,'w') as file:
    pass