import os
current_directory_path=os.getcwd()+"/arjun_j_s/day_11/module_demo"
# os.mkdir(current_directory_path+"/test")
# print(os.listdir(current_directory_path))
# os.remove("test")
print(current_directory_path)

if not os.path.exists(current_directory_path+"/dummy_txt.txt"):
    os.mkdir(current_directory_path+"/dummy_txt")
else:
    os.rename(current_directory_path+"/dummy_txt.txt",current_directory_path+"/final_file.txt")

print(os.listdir(current_directory_path))

