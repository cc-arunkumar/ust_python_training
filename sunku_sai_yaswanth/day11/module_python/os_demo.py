import os
# print("current dictnory",os.getcwd())
# new_dir="sub_dir"
# if not os.path.exists(new_dir):
#     os.mkdir(new_dir)
# else:
#     print("unable create new file")
    
# print(os.mkdir)
# print(os.listdir())
# print(os.remove)
# # print(os.rename())


# print("current dictnory",os.getcwd())
# file="damefile.txt"
# if not os.path.exists(file):
#     os.mkdir(file)
# else:
#     print("unable create new file")
    
# old="damefile.txt"
# new="temp.txt"
# temp=os.rename(old,new)
# print(temp)


target_path = "final_dir"
new_file = "final_report.txt"
if not os.path.exists(target_path):
    os.mkdir(target_path)
    new_file_path = os.path.join(target_path, new_file)
    with open(new_file_path, 'w') as file:
        file.write("this is the final report.")
    print("created new file:", new_file_path)
else:
    print("directory already exists")

    
