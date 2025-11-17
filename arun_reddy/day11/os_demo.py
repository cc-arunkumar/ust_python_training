import os
print(f"current directory path={os.getcwd()}")
print(os.listdir())


if not os.path.exists("sub_dir1"):
    os.mkdir("sub_dir1")
    print(f" sub_dir1 is created successfully")
else:
    print("sub_Dir1 is already exists")


target_path="D:/ust_python_training/arun_reddy/day11/final_dir"
temp="final.txt"
if os.path.exists(target_path):
    print("not exits")
else:
    os.mkdir(target_path)
    print("file created successully")
    
new_path=os.path.join(target_path,temp)
if os.path.exists(new_path):
    print("file already exists")
else:
    with open(new_path,'w') as file:
        pass
    print("file created")
        
    
