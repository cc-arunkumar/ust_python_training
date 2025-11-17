import os
print("current_dir_path= ",os.getcwd())
print(os.listdir())


# if not os.path.exists("sub_dir"):
#     os.mkdir("sub_dir")
# else:
#     print("Already exists")
    
# final_file="final_renamed.txt"

# if not os.path.exists("dummy_file.txt"):
#     os.mkdir("sub_dir\dummy_file.txt")
# else:
#     os.rename("dummy_file.txt",final_file)
    

# # target_path=r"D:\training\ust_python_training\finally_2_dir"
# target_path=r"D:\training\ust_python_training\deva_prasath\day_11\module"+"finally_4"
# new_file="finally_4_report.txt"


# if not os.path.exists(target_path):
#     os.mkdir(target_path)
#     new_finally_last_last=os.path.join(target_path,new_file)
    
# else:
#     print("Already exists")
#     with open ("new_finally_last__last",'w') as file:
#         file.write("heloooo Deavaava prasathh rrr")


import os

target_path=r"D:\training\ust_python_training\deva_prasath\day_11\module" +"finally_5"
new_file="finally_5_report.txt"

if not os.path.exists(target_path):
    os.mkdir(target_path)  
    new_finally_last_last = os.path.join(target_path,new_file)  
else:
    print("Directory already exists")
    new_finally_last_last = os.path.join(target_path, new_file)  

with open(new_finally_last_last, 'w') as file:
    file.write("hello Deavaava prasathh rrr") 
