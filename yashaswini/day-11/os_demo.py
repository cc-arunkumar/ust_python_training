# import os
# target_file="final_file.txt"
# target_path="C:\Users\Administrator\Desktop\training\ust_python_training\yashaswini"
# new_file="final_report.txt"
# directory=os.path.dirname(target_path)
# if not os.path.exists(directory):
#     os.makedirs(directory)
#     print("directory created")
# else:
#      print("directory already exists")
     
# if not os.path.exists    

import os
target = "final_dir"
new_file = "final_report.txt"

if not os.path.exists(target):
    os.mkdir(target)
    print("Directory created")
else:
    print("Path already exists")

file_path = os.path.join(target, new_file)

if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        file.write() 
