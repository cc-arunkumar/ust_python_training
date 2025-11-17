import os
# print("Current Working Directory:", os.getcwd())
# print(os.listdir())

# new_dir="sub_dir"
# if not os.path.exists(new_dir):
#     os.mkdir(new_dir)
#     print("Directory sub_dir created.")
# else:
#     print("Directory sub_dir already exists.")
    
# temp="dummy_file.txt"
# if not os.path.exists(temp):
#     with open(temp,'w') as f:
#         f.write("This is a dummy file.")
#     print("File dummy_file.txt created.")
# else:
#     file1="final_file.txt"
#     os.rename(temp,file1)
#     print("File renamed to final_file.txt")

# print(os.listdir())

target_path = "C:\\Users\\Administrator\\Desktop\\Training\\ust_python_training\\harsh\\day11\\module\\final_dir"
new_file = "final_report.txt"
full_path = os.path.join(target_path, new_file)
print(full_path)

if not os.path.exists(target_path):
    print("final_dir does not exist.")
    os.mkdir(target_path)
    print("Directory final_dir created.")
    print(f"File will be created at: {full_path}")
    with open(full_path, 'w') as f:
        f.write("This is the final report.")
    print("File final_report.txt created in current directory as sub_dir does not exist.")
else:
    print("sub_dir exists.")
   
    print(f"File will be created at: {full_path}")