# Search Employee by ID
# Ask the user for an Employee ID.
# Search the file line by line.
# If found, display the employee details.
# If not found, print a message “Employee not found.”


import os

e_id = "E101"
if os.path.exists("employee.txt"):
    with open("employee.txt", "r") as file:
        flag =False
        for line in file:
            tokens = line.strip().split(",")
            employee_id = tokens[0]
            if employee_id ==e_id:
                print(f"Employee found {line}")
                flag=True
                break
            
            print(line.strip())
        if flag==False:
            print("Employee not found")
            
else:
    print("File not found")
    
    
    
# ========Sample output===========
# Employee found E101,Neha Sharma,HR,60000,2020-05-10