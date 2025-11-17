import os  # Import the os module \

# Print the current working directory path
print("Current directory path =", os.getcwd())  

# List all files and directories in the current directory
print(os.listdir())  # os.listdir() returns a list of all files and directories in the current directory

# Define the file name
file1 = "dummy_file.txt"

# Check if the file "dummy_file.txt" does not exist
if not os.path.exists(file1):  # os.path.exists() checks if a file or directory exists
    os.mkdir("dummy_file.txt")  # os.mkdir() creates a directory
else:
    # Rename the directory "dummy_file.txt" to "final_file.txt" if it exists
    os.rename("dummy_file.txt", "final_file.txt")  


#Sample Output
# ['.git', 'ashutosh_samal', 'UST_Order_Processing'] #List all files and directories in the current directory