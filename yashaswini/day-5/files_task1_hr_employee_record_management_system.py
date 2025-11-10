#hr employee record management system

# Functional Requirements
# Your program must provide the following 6 major operations.
# Each operation should be implemented as a separate function.
# Add New Employee
# Ask the user to enter new employee details.
# Append this record to the existing employees.txt file.
# Validate that the EmployeeID is unique (no duplicates).
# Example input:
# Enter Employee ID: E106
# Enter Name: Meera Nair
# Enter Department: HR
# Text File Task 2
# Enter Salary: 64000
# Enter Joining Date (YYYY-MM-DD): 2022-11-20
# Append the record:
# E106,Meera Nair,HR,64000,2022-11-20
# Display All Employees
# Read and print all records neatly formatted.
# Handle case when the file is empty.
# Example output:
# Employee Records:
# E101 | Neha Sharma | HR | 60000 | 2020-05-10
# E102 | Ravi Kumar | IT | 75000 | 2019-08-21
# ...
# Search Employee by ID
# Ask the user for an Employee ID.
# Search the file line by line.
# If found, display the employee details.
# If not found, print a message “Employee not found.”
# Example:
# Enter Employee ID to search: E103
# Employee Found:
# E103 | Arjun Mehta | Finance | 55000 | 2021-03-15
# Update Employee Salary
# Text File Task 3
# Ask for Employee ID and new salary.
# Read all lines, modify the correct line, and rewrite the file with the updated
# data.
# Example:
# Enter Employee ID: E104
# Enter New Salary: 65000
# Result:
# E104,Fatima Khan,HR,65000,2018-12-05
# Generate Department-wise Summary Report
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
# Delete Employee Record
# Ask for Employee ID to delete.
# Read all lines, remove the matching record, and rewrite the file.
# Text File Task 4
# Confirm deletion to the user.
# Example:
# Enter Employee ID to delete: E105
# Employee deleted successfully


import os
from datetime import datetime

with open("employees.txt", "w") as file:
    file.write("E101,Neha Sharma,HR,60000,2020-05-10\n")
    file.write("E102,Ravi Kumar,IT,75000,2019-08-21\n")
    file.write("E103,Arjun Mehta,Finance,55000,2021-03-15\n")
    file.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
    file.write("E105,Vikram Singh,Operations,58000,2022-01-11\n")


with open("employees.txt", "a") as file:
    file.write("E106,Yashaswini,HR,64000,2022-11-20\n")


if not os.path.exists("employees.txt") or os.path.getsize("employees.txt") == 0:
    print("No employee records found.")
else:
    print("Employee Records:")
    with open("employees.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            print(" | ".join(parts))
            
                
emp_id = input("Enter Employee ID to search: ").strip()
found = False
with open("employees.txt", "r") as file:
    for line in file:
        if line.startswith(emp_id + ","):
            print("Employee Found:")
            print(" | ".join(line.strip().split(",")))
            found = True
            break
if not found:
    print("Employee not found.")


 
emp_id = input("Enter Employee ID: ").strip()
new_salary = input("Enter New Salary: ").strip()
updated_lines = []
with open("employees.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if parts[0] == emp_id:
            parts[3] = new_salary  
        updated_lines.append(",".join(parts))
with open("employees.txt", "w") as file:
    for line in updated_lines:
        file.write(line + "\n")

print("Salary updated successfully!")

dept_summary = {}
with open("employees.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        dept = parts[2]
        salary = float(parts[3])
        if dept not in dept_summary:
            dept_summary[dept] = {"count": 0, "total": 0}
        dept_summary[dept]["count"] += 1
        dept_summary[dept]["total"] += salary
        
with open("report.txt", "w") as file:
    for dept, data in dept_summary.items():
        avg_salary = data["total"] / data["count"]
        file.write(f"{dept} Department -> Employees: {data['count']} | "
                   f"Total Salary: {data['total']} | Average Salary: {avg_salary:.1f}\n")

print("\nReport generated successfully")



emp_id = input("\nEnter Employee ID to delete: ").strip()
lines = []
deleted = False
with open("employees.txt", "r") as file:
    for line in file:
        if not line.startswith(emp_id + ","):
            lines.append(line)
        else:
            deleted = True
with open("employees.txt", "w") as file:
    for line in lines:
        file.write(line)
if deleted:
    print("Employee deleted successfully")
else:
    print("Employee not found.")
    

#o/p:
# Employee Records:
# E101 | Neha Sharma | HR | 60000 | 2020-05-10
# E102 | Ravi Kumar | IT | 75000 | 2019-08-21
# E103 | Arjun Mehta | Finance | 55000 | 2021-03-15
# E104 | Fatima Khan | HR | 62000 | 2018-12-05
# E105 | Vikram Singh | Operations | 58000 | 2022-01-11
# E106 | Yashaswini | HR | 64000 | 2022-11-20
# Enter Employee ID to search: E103
# Employee Found:
# E103 | Arjun Mehta | Finance | 55000 | 2021-03-15
# Enter Employee ID: E104
# Enter New Salary: 65000
# Salary updated successfully!

# Report generated successfully

# Enter Employee ID to delete: E105
# Employee deleted successfully