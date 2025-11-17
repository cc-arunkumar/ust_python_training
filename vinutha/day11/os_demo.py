# import os
# print("current directory path:",os.getcwd())
# # print(os.mkdir)
# print(os.listdir())#list the files
# # print(os.remove('remove.py'))
# # print(os.rename()

# import os
# new_dir = "sub_dir"
# if not os.path.exists(new_dir):
#     os.mkdir(new_dir)
#     print(f"New path '{new_dir}' was created.")
# else:
#     print(f"The path '{new_dir}' already exists.")

# print(os.listdir())

# import os
# new_dir = "sub_dir"
# file1 = "final_file.txt" 
# if not os.path.exists(new_dir):
#     os.mkdir(new_dir)
#     print(f"New path '{new_dir}' was created.")
# else:
#     if os.path.exists('dummy_file.txt'):
#         os.rename('dummy_file.txt', file1)
#         print(f"File has been renamed to '{file1}'.")
#     else:
#         print("The file 'dummy_file.txt' does not exist.")

   
# target = "final_dir"
# new_file = "final_report.txt"

# if not os.path.exists(target):
#     os.mkdir(target)
#     print("Directory created")
# else:
#     print("Path already exists")

# file_path = os.path.join(target, new_file)

# if not os.path.exists(file_path):
#     with open(file_path, "w") as file:
#         file.write() 




import os
target_path = "sub_dir"
new_file = "final_report.txt"
new_file_path = os.path.join(target_path, new_file)
if not os.path.exists(target_path):
    os.mkdir(target_path)
    print(f"Dir'{target_path}' was created.")
if not os.path.exists(new_file_path):
    with open(new_file_path, 'w') as file:
        file.write("This is the final report.")
    print(f"File '{new_file}' was created and written to.")
else:
    print(f"The file '{new_file}' already exists.")



