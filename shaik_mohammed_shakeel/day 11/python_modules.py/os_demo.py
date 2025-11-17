import os
# print("Current Directory Path",os.getcwd())
# print("Current Directory Path",os.mkdir)
# print("Current Directory Path",os.listdir())
# print("Current Directory Path",os.remove)
# print("Current Directory Path",os.rename())

#mkdir
# new_dir="sub_dir"
# if not os.path.exists("new_dir"):
#     print(os.mkdir(new_dir))
# else:
#     print("Not Existed")


# print("Current Directory Path",os.listdir())
# file1 = "file1.txt" 

# if os.path.exists(file1):
#     new_name = "updated.txt"
#     os.rename(file1, new_name)
#     print(f"{new_name}")
# else:
#     with open(file1, "w") as f:
#         f.write("")
#     print(f"File not exist. Created '{file1}'")

# target_path="final.txt"
# new_file="final_report.txt"
# if not os.exists(target_path):
#     print("File Not Exists and created new one")
# else:
#     new_file_path=os.path.join(target_path,new_file)
#     with open("new_file_path","w",newline=)as file




target_path = os.getcwd() + '/final_dir'
new_file = "final_report.txt"

if not os.path.exists(target_path):
    os.mkdir('final_dir')
        
else:
    print("File Existed")

new_file_path = os.path.join(target_path, new_file)
with open(new_file_path, 'w') as file:
    pass
        
