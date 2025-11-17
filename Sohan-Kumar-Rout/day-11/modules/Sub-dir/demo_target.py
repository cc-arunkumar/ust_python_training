
import os 

target_path = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-11\modules\Sub-dir"
new_file = "final_report.txt"

os.makedirs(target_path, exist_ok=True)

file_path = os.path.join(target_path, new_file)

if not os.path.exists(file_path):
    print("File does not exist, creating...")
else:
    print("File already exists, overwriting...")

with open(file_path, "w", newline="") as file:
    file.write("This is the start of the final report.\n")

print("Done. File path:", file_path)

