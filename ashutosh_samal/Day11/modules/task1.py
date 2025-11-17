import os  # Import the os module to interact with the operating system

# Define the target path where the directory and file will be created
target_path = r"C:\Users\Administrator\Desktop\training\ust_python_training\ashutosh_samal\Day11\modules" + "final"
new_file = "final_report_.txt"  # Name of the new file to be created

# Check if the target directory does not exist
if not os.path.exists(target_path):  # os.path.exists() checks if the path exists
    os.mkdir(target_path)  # Create the directory if it does not exist
    # Combine the target path and new file name to get the full path for the new file
    new_final_path = os.path.join(target_path, new_file)
else:
    # If the directory already exists, just combine the target path and file name
    new_final_path = os.path.join(target_path, new_file)

# Open the file in write mode ("w"), this will create the file if it doesn't exist
with open(new_final_path, "w") as file:  # Use new_final_path to specify the full path of the file
    file.write("welcome")  # Write the string "welcome" to the file
