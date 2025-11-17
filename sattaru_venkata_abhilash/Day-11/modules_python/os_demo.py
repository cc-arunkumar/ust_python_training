import os
import csv

# Print the current working directory path
print("current directory path=", os.getcwd())

# Define a new directory name and a file name
new_dir = "sub_dir"
file1 = "final_file.txt"

# Check if final_file.txt exists
# If NOT exists → create it
if not os.path.exists(file1):
    with open(file1, "w") as file:
        # Creating a CSV DictWriter object (not writing anything now)
        writer = csv.DictWriter(file, fieldnames="")
else:
    # If file exists → rename dummy_file.txt → final_file.txt
    os.rename("dummy_file.txt", file1)

# Print all files and folders in current directory after operations
print("current directory path=", os.listdir())

# Rename a file from new.txt → os_get_demo.txt
# os.rename() does NOT return anything, so it prints None
print("current directory path=", os.rename("new.txt", "os_get_demo.txt"))

# Delete the file os_get_demo.txt
# os.remove() also returns None
print("current directory path=", os.remove("os_get_demo.txt"))

# Print the current directory again
print("current directory path=", os.getcwd())

# Create a new path for directory 'final_dir'
target_path = os.getcwd() + '/final_dir'

# Name of a new file that will be created inside final_dir
new_file = "final_report.txt"

# Check if final_dir already exists
# If NOT → create the directory
if not os.path.exists(target_path):
    os.mkdir('final_dir')
else:
    print("Dir Already Exists....")

# Create full file path by joining the directory path and file name
new_file_path = os.path.join(target_path, new_file)

# Create the new empty file inside final_dir
with open(new_file_path, 'w') as file:
    pass   # Using pass means: do nothing (just create the file)


# sample output:
# current directory path= C:\Users\Abhi\PythonProjects

# current directory path= ['final_file.txt', 'dummy_file.txt', 'new.txt', 'main.py']

# None

# None

# current directory path= C:\Users\Abhi\PythonProjects

# Dir Already Exists....
