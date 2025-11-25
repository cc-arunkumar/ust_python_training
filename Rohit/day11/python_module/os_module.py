import os   # Import the os module for file and directory operations

# Example (commented out):
# print("Current Working Directory:", os.getcwd())   # Prints current working directory
# file_path = os.path.join(os.getcwd(), "new_file.txt")   # Creates a file path in current directory
# print("File Path:", file_path)   # Prints the file path
# print("list of files and directories in current directory:", os.listdir(os.getcwd()))   # Lists files/folders

# Define full path to the new folder
new_folder = r"C:\Users\Administrator\Desktop\ust_python_training\rohit\dummy"

# Define file name
file_name = "dummy_file.txt"

# Create full file path by joining folder and file name
file_path = os.path.join(new_folder, file_name)

# Print the file path (for debugging/confirmation)
print(file_path)

# Check if the folder exists
if not os.path.exists(new_folder):
    # If folder does not exist, create it
    os.mkdir(new_folder)

    # Create and open the dummy file inside the new folder
    with open(file_path, "w") as f:
        f.write("this is dummy file")   # Write text into the file

    # Confirmation message
    print(f"File '{file_name}' created in {new_folder}")
else:
    # If folder already exists, print message
    print("already exist")

