import os

# print("current directory path: ",os.getcwd())
# print("list directory",os.listdir())
# if not os.path.exists("sub_dir"):
#     os.mkdir("sub_dir")
# else:
#     print("already exists")
# print("list directory",os.listdir())


target_path=os.getcwd()+"/final_dir"
new_file="final_report.txt"

if not os.path.exists(target_path):
    os.mkdir("final_dir")
else:
    print("already exists")

new_path=os.path.join(target_path,new_file)
with open(new_path,"w") as file:
    pass
    
    

