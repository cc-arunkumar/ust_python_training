import os

target_path = r"C:\Users\Administrator\Desktop\Training\ust_python_training\sovan__mohanty\day11\python_module\sub_dir"
new_file = "final_report.txt"

os.makedirs(target_path, exist_ok=True)

full_path = os.path.join(target_path, new_file)

if not os.path.exists(full_path):
    print("File does not exist, creating the file...")
else:
    print("File path exists, overwriting the file...")

with open(full_path, 'w', newline="") as f:
    f.write("This is the final report.\n")

#Sample Execution
# File path exists, overwriting the file..