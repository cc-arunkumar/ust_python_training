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
        file.write("gfshjdc") 
        print("file created")


