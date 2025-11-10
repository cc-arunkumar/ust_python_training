# HR Employee Record Management System
# Objective
# Design a simple Python file handling program that manages employee
# information using .txt files.
# The program should allow adding, reading, searching, updating, and summarizing
# employee records — all stored in plain text format.
# Participants will build this system from scratch, practicing all file operations ( read ,
# write , append , seek , etc.) while maintaining data consistency.
# Concepts Covered
# File creation and writing
# Reading data line-by-line
# Appending new data
# Searching within a file
# Counting and summarizing data
# Writing formatted reports to a new file
# Technical Requirements
# Requirement Details
# File Type Used .txt files
# Modules Allowed Only built-in modules ( os , datetime )
# Primary File employees.txt (stores all employee records)
# Text File Task 1
# Requirement Details
# Report File report.txt (generated summary report)
# Data Format in File One record per line, comma-separated:
# EmployeeID,Name,Department,Salary,JoiningDate
# Example Record E101,Neha Sharma,HR,60000,2020-05-10
# Initial Setup
# Create a text file named employees.txt in the same folder as your Python script.
# Put in some sample data (5–6 records):
# E101,Neha Sharma,HR,60000,2020-05-10
# E102,Ravi Kumar,IT,75000,2019-08-21
# E103,Arjun Mehta,Finance,55000,2021-03-15
# E104,Fatima Khan,HR,62000,2018-12-05
# E105,Vikram Singh,Operations,58000,2022-01-11
#Functional Requirements
# Your program must provide the following 6 major operations.
# Each operation should be implemented as a separate function.
import os 
with open('employees.txt','w') as file:
    file.write("E101,Neha Sharma,HR,60000,2020-05-10\n")
    file.write("E102,Ravi Kumar,IT,75000,2019-08-21\n")
    file.write("E103,Arjun Mehta,Finance,55000,2021-03-15\n") 
    file.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
    file.write("E105,Vikram Singh,Operations,58000,2022-01-11\n")

#1.Add New Employee
    # Ask the user to enter new employee details.
    # Append this record to the existing employees.txt file.
    # Validate that the EmployeeID is unique (no duplicates).
    # Example input:
    # Enter Employee ID: E106
    # Enter Name: Meera Nair
    # Enter Department: HR
    # Enter Salary: 64000
    # Enter Joining Date (YYYY-MM-DD): 2022-11-20
    # Append the record:
    # E106,Meera Nair,HR,64000,2022-11-20
def new_employee():
    e_id = input("Enter Employee ID:")
    name = input("Enter Name: ")
    dept = input("Enter Department:")
    salary = int(input("Enter Salary:"))
    doj = input("Enter Joining Date(YYYY-MM-DD):")
    found = False
    with open('employees.txt','r') as file:
        for lines in file:
            li=lines.split(',')
            if li[0]==e_id:
                print("Employee ID Already Exist")
                found = True
                break
    if not found:
        with open('employees.txt','a') as file:
            file.write(f'{e_id},{name},{dept},{salary},{doj}')
        print("Employee Details Added Successfully!")

# 2. Display All Employees
# Read and print all records neatly formatted.
# Handle case when the file is empty.
# Example output:
# Employee Records:
# E101 | Neha Sharma | HR | 60000 | 2020-05-10
# E102 | Ravi Kumar | IT | 75000 | 2019-08-21

def display_employees():
    if os.path.exists('employees.txt'):
        with open('employees.txt','r') as file:
            for line in file:
                li = line.strip().split(",")
                print(" | ".join(li))

# 3.Search Employee by ID
# Ask the user for an Employee ID.
# Search the file line by line.
# If found, display the employee details.
# If not found, print a message “Employee not found.”
# Example:
# Enter Employee ID to search: E103
# Employee Found:
# E103 | Arjun Mehta | Finance | 55000 | 2021-03-15

def search_id():
    e_id = input("Enter the Employee ID to search:")
    with open("employees.txt","r") as file:
        is_found = False
        for line in file:
            li = line.strip().split(",")
            if li[0]==e_id:
                is_found =True
                print(" | ".join(li)) 
        if not is_found:
            print("Employee not found")

# 4.Update Employee Salary
# Ask for Employee ID and new salary.
# Read all lines, modify the correct line, and rewrite the file with the updated
# data.
# Example:
# Enter Employee ID: E104
# Enter New Salary: 65000
# Result:
# E104,Fatima Khan,HR,65000,2018-12-05

def update_salary():
    e_id = input("Enter Employee ID:")
    updated_sal = input("Enter New Salary:")
    with open("employees.txt","r") as file:
        lines = file.readlines()
        is_found = False
        i=0
        for line in lines:
            li = line.strip().split(",")
            if li[0]==e_id:
                is_found =True
                li[3]=updated_sal
                print(",".join(li))
                lines[i] = ",".join(li)
                lines[i] = lines[i]+"\n"
            i += 1
        if not is_found:
            print("Employee not found")
    with open("employees.txt","w") as file:
        file.writelines(lines)

# 5.Generate Department-wise Summary Report
# Read all employee records.
# Count how many employees work in each department.
# Calculate total and average salary per department.
# Write the summary to a new file called report.txt .
# Example output in report.txt :
# HR Department → Employees: 3 | Total Salary: 186000 | Average Salary: 6200
# 0.0
# IT Department → Employees: 1 | Total Salary: 75000 | Average Salary: 75000.0
# Finance Department → Employees: 1 | Total Salary: 55000 | Average Salary: 5
# 5000.0
# Operations Department → Employees: 1 | Total Salary: 58000 | Average Salar
# y: 58000.0

def summary():
    if os.path.exists('employees.txt'):
        with open('employees.txt','r') as file:
            dic_store={}
            for line in file:
                li = line.strip().split(",")
                if li[2] not in dic_store.keys():
                    dic_store[li[2]] = [float(li[3])]
                else:
                    dic_store[li[2]].append(float(li[3]))
            for key,value in dic_store.items():
                count = len(value)
                total_sal = sum(value)
                avg_sal = total_sal/count
                with open("report.txt","a") as file:
                    file.write(f"{key} Department -> Employees: {count} | Total Salary: {total_sal} | Average Salary: {avg_sal}\n")
            print("Report Created Successfully!")

# 6. Delete Employee Record
# Ask for Employee ID to delete.
# Read all lines, remove the matching record, and rewrite the file.
# Text File Task 4
# Confirm deletion to the user.
# Example:
# Enter Employee ID to delete: E105
# Employee deleted successfully!

def delete_employee():
    e_id = input("Enter Employee ID to delete:")
    with open("employees.txt","r") as file:
        lines = file.readlines()
        is_found = False
        i=0
        for line in lines:
            li = line.strip().split(",")
            if li[0]==e_id:
                is_found =True
                lines.pop(i)
                print("Employee deleted Successfully!")
                break
            i += 1
        if not is_found:
            print("Employee not found")
    with open("employees.txt","w") as file:
        file.writelines(lines)

print("==== Employee Record Management ====")
print("1. Add New Employee")
print("2. Display All Employees")
print("3. Search Employee by ID")
print("4. Update Employee Salary")
print("5. Generate Department Report")
print("6. Delete Employee")
print("7. Exit")


while(True):
    ip=int(input("Enter your choice:"))
    if ip==1:
        new_employee()
    elif ip==2:
        display_employees()
    elif ip==3:
        search_id()
    elif ip==4:
        update_salary()
    elif ip==5:
        summary()
    elif ip==6:
        delete_employee()
    elif ip==7:
        print("Exitted Sucessfully!")
        break 
    else:
        print("Invalid Input")


#Sample Output
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit

# Enter your choice:2
# E101 | Neha Sharma | HR | 60000 | 2020-05-10
# E102 | Ravi Kumar | IT | 75000 | 2019-08-21
# E103 | Arjun Mehta | Finance | 55000 | 2021-03-15
# E104 | Fatima Khan | HR | 62000 | 2018-12-05
# E105 | Vikram Singh | Operations | 58000 | 2022-01-11

# Enter your choice:3
# Enter the Employee ID to search:E102
# E102 | Ravi Kumar | IT | 75000 | 2019-08-21

# Enter your choice:4
# Enter Employee ID:E104
# Enter New Salary:43200
# E104,Fatima Khan,HR,43200,2018-12-05

# Enter your choice:5
# Report Created Successfully!
# report.txt
    # HR Department -> Employees: 2 | Total Salary: 122000.0 | Average Salary: 61000.0
    # IT Department -> Employees: 1 | Total Salary: 75000.0 | Average Salary: 75000.0
    # Finance Department -> Employees: 1 | Total Salary: 55000.0 | Average Salary: 55000.0
    # Operations Department -> Employees: 1 | Total Salary: 40000.0 | Average Salary: 40000.0
    # HR Department -> Employees: 2 | Total Salary: 103200.0 | Average Salary: 51600.0
#Enter your choice:6
# Enter Employee ID to delete:E105
# Employee deleted Successfully!