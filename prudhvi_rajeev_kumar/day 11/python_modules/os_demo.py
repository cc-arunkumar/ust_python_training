import os
# print("Current Working Directory:", os.getcwd())

# mkdir = "sample_dir"
# list_dir = os.listdir()
# print("Directory List before creating new directory:", list_dir)

# os.mkdir(mkdir)
# os.rename("sample_dir", "renamed_dir")
# os.remove("renamed_dir")
# new_dir = "sub_dir"

# if not os.path.exists("new_dir"):
#     os.mkdir("sub_dir")
#     print(f"Directory '{new_dir}' created.")
# else:
#     print(f"Directory '{new_dir}' already exists.")

# list_dir = os.listdir()
# print("Directory List before creating new directory:", list_dir)
   
# new_dir1 = "file.txt"
# if os.path.exists("new_dir1"):
#     os.rename("file.txt", "final_file.txt")
#     print(f"Name has been changed to 'final_file.txt'.")
# else:
#     print(f"The file doesnot exists")

target_path = os.path.join(os.getcwd()+"/day 11/python_modules", "final_dir")
new_file = "final_report.txt"
if not os.path.exists(target_path):
    os.mkdir(target_path)
    print(f"Directory has been created as it doesnot exists!.")
else:
    new_file_path = os.path.join(target_path, new_file)
    with open(new_file_path, 'w') as f:
        f.write("This is the final report.")
    print(f"File created inside the directory.")
