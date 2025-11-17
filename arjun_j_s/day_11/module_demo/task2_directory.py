import os
current_directory_path=os.getcwd()+"/arjun_j_s/day_11/module_demo"

if not os.path.exists(current_directory_path+"/final_dir"):
    print("No Directory Creating....")
    os.mkdir(os.path.join(current_directory_path,"final_dir"))
else:
    with open(current_directory_path+"/final_dir/final_report.txt", "w") as file:
        file.write("Write successfull")
    print("Writed !!")