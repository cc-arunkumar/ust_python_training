import os
# print("Current Directory Path=",os.getcwd())

# print("Current Directory Path=",os.listdir())
# print("Current Directory Path=",os.remove())
# print("Current Directory Path=",os.rename(old,new))

# new_dir = "sub_dir"    ## print("Current Directory Path=",os.mkdir())
# if not os.path.exists("new_dir"):
#     print(os.mkdir(new_dir))
# else:
#     print("Failed")


# print("Current Directory Path=",os.listdir())

# -------------------------------------------------------------------

# file1 = "final_file.txt"
# if not os.path.exists(file1):
#     with open(file1, "w") as file:
#         file.write("")
#     print(f"File '{file1}' created.")
# else:
#     old_file = "dummy_file.txt"
#     if os.path.exists(old_file):
#         os.rename(old_file, file1)
#         print(f"Renamed '{old_file}' to '{file1}'.")
    

target_path = os.getcwd() + '/final'
new_file = "final_report.txt"

if not os.path.exists(target_path):
    os.mkdir("final")
else:
    new_file_path = os.path.join(target_path, new_file)
    if not os.path.exists(new_file_path):
        with open(new_file_path, "w") as f:
            f.write("")
        print(f"File '{new_file}' created at '{target_path}'.")
    else:
        print(f"File '{new_file}' already exists at '{target_path}'.")









