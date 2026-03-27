# This code checks if a directory named final_dir exists; if not, it creates it. Then, it creates a file called final_report.
# txt inside that directory, writing a sample message to it.

import os

# Print current working directory
print("Current directory path:", os.getcwd())

# List the contents of the current directory
print("List of files and directories:", os.listdir())

# Check if the target directory exists
target_path = os.path.join(os.getcwd(), "final_dir")
new_file = "final_report.txt"

# Create 'final_dir' if it doesn't exist
if not os.path.exists(target_path):
    os.mkdir(target_path)
    print(f"Directory '{target_path}' created.")
else:
    print(f"Directory '{target_path}' already exists.")

# Create a new file within 'final_dir'
new_path = os.path.join(target_path, new_file)

# Create the file (or overwrite it) if it doesn't already exist
with open(new_path, "w") as file:
    file.write("This is the final report.\n")  # Writing sample content to the file
    print(f"File '{new_file}' has been created in '{target_path}'.")

# List contents of 'final_dir' to verify the creation of the file
print("Contents of 'final_dir':", os.listdir(target_path))

    