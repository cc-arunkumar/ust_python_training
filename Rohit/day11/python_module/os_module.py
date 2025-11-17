import os

# print("Current Working Directory:", os.getcwd())
# "make file path"
# file_path = os.path.join(os.getcwd(), "new_file.txt")
# print("File Path:", file_path)
# print("list of files and directories in current directory:", os.listdir(os.getcwd()))



# Full path to the new folder

# # Check if folder exists, if not create it
# if not os.path.exists(new_folder):
#     os.mkdir(new_folder)
#     os.path.join(new_folder,"dummy_file.txt")
#     print(f"Directory '{new_folder}' created.")
# else:
#     print(os.rename(new_folder,"rohit"))


new_folder = r"C:\Users\Administrator\Desktop\ust_python_training\rohit\dummy"
file_name = "dummy_file.txt"
file_path = os.path.join(new_folder, file_name)
print(file_path)
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    with open(file_path, "w") as f:
        f.write("this is dummy file")

    print(f"File '{file_name}' created in {new_folder}")
else:
    print("already exist")
