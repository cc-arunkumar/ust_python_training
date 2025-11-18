import os
current_directory_path=os.getcwd()
print(current_directory_path)
current_directory_path=os.listdir()
print(current_directory_path)

newdir="sub_dir"
if not os.path.exists(newdir):
    os.mkdir(newdir)
    
    
import os
# old_file ="sub_dir/dummy_file.txt"
# new_file = "sub_dir/final_file.txt"

# if os.path.exists(old_file):

#     os.rename(old_file, new_file)
#     print(f"File renamed to {new_file}")
# else:
#     with open(old_file, "w") as f:
#         f.write("")  
#     print(f"File {old_file} created as it didn't exist.")




import os
path = "sub_dir"
newpath = "final_report.txt" 
new_file = os.path.join(path, newpath)

if not os.path.exists(new_file):
    with open(new_file, 'w') as f:
        f.write("")  
    print(f"File {new_file} created.")
else:
    print(f"File {new_file} already exists.")


    

