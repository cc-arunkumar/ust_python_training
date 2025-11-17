import os

print("Current directory path = ",os.getcwd())
print(os.listdir())

if not os.path.exists("sub_dir"):
    os.mkdir("sub_dir")
else:
    print("Diarectory already exist")
    
if not os.path.exists("dummy_file.txt"):
    with open("final_file.txt")as file:
        pass
else:
    os.rename("dummy_file.txt","final_file.txt")
    
target_path = "C:/Users/Administrator/Desktop/ust_python_training-1/felix/day-11/final_dir"
new_file = "final_report.txt"

if os.path.exists(target_path):
    print("Directory Already exist")
else:
    os.mkdir(target_path)
    
new_path = os.path.join(target_path,new_file)
if os.path.exists(new_path):
    print("File already exist")
else:
    with open(new_path,"w") as file:
        pass