# Display All Employees
# Read and print all records neatly formatted.
# Handle case when the file is empty.
# Example output:
# Employee Records:
# E101 | Neha Sharma | HR | 60000 | 2020-05-10
# E102 | Ravi Kumar | IT | 75000 | 2019-08-21
# ...

import os   # Import the os module to check if a file exists

def read():
    # Check if the file 'employees.txt' exists in the current directory
    if os.path.exists("employees.txt"):
        # Open the file in read mode
        with open("employees.txt", "r") as file:
            # Read the entire content of the file
            content = file.read()
            # Print the content to the console
            print(content)
    else:
        # If the file does not exist, print a message
        print("does not exist")



