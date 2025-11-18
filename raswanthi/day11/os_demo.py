#importing os
import os 
#getting current directory details
current_directory_path=os.getcwd()
list_dir_details=os.listdir(current_directory_path)

print(current_directory_path)
print(list_dir_details)

# new_dir="sub_dir"
# if not os.path.exists(new_dir):
#     os.mkdir(new_dir)
    
# file1="final_file.txt"
# if not os.path.exists(file1):
#     with open(file1, "w", encoding="utf-8") as f:
#         f.write()

# else:
#     os.rename("dummy_file.txt",file1)
    

    
target = "final_dir"
new_file = "final_report.txt"

if not os.path.exists(target):
    os.mkdir(target)
    print("Directory created")
else:
    print("Path already exists")

file_path = os.path.join(target, new_file)

if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        file.write() 
