import os
# print("Current directory path",os.getcwd())
# mkdir="sample_dir"
# list_dir=os.listdir()
# print("directory list before creating new dir:",list_dir)
# os.mkdir(mkdir)
# os.rmdir(mkdir)

# new_dir = "sub_dir"
# if not os.path.exists("sub_dir"):
#     os.mkdir("sub_dir")
#     print(f"Directory '{new_dir}' created.")
# else:
#     print(f"Directory '{new_dir}' already exists")
# # print(os.listdir)
# temp = "dummy_file.txt"
# if  os.path.exists("temp"):
#     os.rename("dummy_file.txt","final_file.txt")
#     print(f"path already exits",final_file.txt)
# else:
#     file1="final_file.txt"
#     os.rmdir
print(os.getcwd())
# target_path =os.path.join(os.getcwd()+"/day11/python_modules","final_dir")
# new_file = "final_report.txt"
# if not os.path.exists(target_path):
#     os.mkdir(target_path)
#     print(f"directory created")
# else:
#     new_file_path=os.path.join(target_path,new_file)
#     with open(new_file,'w') as file:
#         file.write("final report")
#     print(f"file created")
    
new_folder = r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\dummy"
file_name = "dummy_file.txt"
file_path = os.path.join(new_folder,file_name)

print(file_path)
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    with open(file_path, mode="w") as f:
        f.write("hello from taniya side")
else:
    print("Already exists")

    