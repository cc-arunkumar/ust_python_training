# HR Employee Record Management System

# Text File Task
# HR Employee Record Management
# System
# Objective
# Design a simple Python file handling program that manages employee
# information using .txt files.
# The program should allow adding, reading, searching, updating, and summarizing
# employee records — all stored in plain text format.
# Participants will build this system from scratch, practicing all file operations ( read ,
# write , append , seek , etc.) while maintaining data consistency.

# Initial Setup
# Create a text file named employees.txt in the same folder as your Python script.
# Put in some sample data (5–6 records):
# E101,Neha Sharma,HR,60000,2020-05-10
# E102,Ravi Kumar,IT,75000,2019-08-21
# E103,Arjun Mehta,Finance,55000,2021-03-15
# E104,Fatima Khan,HR,62000,2018-12-05
# E105,Vikram Singh,Operations,58000,2022-01-11

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
# Employee deleted successfully!
# Program Flow (Menu Driven)

# When the program runs, show a simple menu like this:
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit

# Enter your choice:
# Use a while True loop and break when user chooses Exit.

import os
from datetime import datetime

# Okay, first I’ll define file names to store employee data and reports
EMPLOYEE_FILE = 'employees.txt'
REPORT_FILE = 'report.txt'

# Function to add a new employee
def add_employee():
    # Let’s start by asking for Employee ID
    emp_id = input("Enter Employee ID: ").strip()
    if not emp_id:
        print("Employee ID cannot be empty.")
        return

    # Now I’ll check if this ID already exists in the file
    if os.path.exists(EMPLOYEE_FILE):
        with open(EMPLOYEE_FILE, 'r') as f:
            for line in f:
                if line.startswith(emp_id + ','):
                    print("Employee ID already exists.")
                    return

    # Collecting other details now
    name = input("Enter Name: ").strip()
    dept = input("Enter Department: ").strip()
    try:
        salary = float(input("Enter Salary: ").strip())
    except ValueError:
        print("Invalid salary. Must be a number.")
        return
    join_date = input("Enter Joining Date (YYYY-MM-DD): ").strip()

    # Validating date format
    try:
        datetime.strptime(join_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format.")
        return

    # Finally, I’ll write this record into the file
    with open(EMPLOYEE_FILE, 'a') as f:
        f.write(f"{emp_id},{name},{dept},{salary},{join_date}\n")
    print("Employee added successfully!")

# Function to display all employees
def display_employees():
    # First check if file exists and has data
    if not os.path.exists(EMPLOYEE_FILE) or os.path.getsize(EMPLOYEE_FILE) == 0:
        print("No employee records found.")
        return

    print("Employee Records:")
    with open(EMPLOYEE_FILE, 'r') as f:
        for line in f:
            emp_id, name, dept, salary, join_date = line.strip().split(',')
            print(f"{emp_id} | {name} | {dept} | {salary} | {join_date}")

# Function to search employee by ID
def search_employee():
    emp_id = input("Enter Employee ID to search: ").strip()
    found = False
    with open(EMPLOYEE_FILE, 'r') as f:
        for line in f:
            if line.startswith(emp_id + ','):
                emp_id, name, dept, salary, join_date = line.strip().split(',')
                print("Employee Found:")
                print(f"{emp_id} | {name} | {dept} | {salary} | {join_date}")
                found = True
                break
    if not found:
        print("Employee not found.")

# Function to update salary
def update_salary():
    emp_id = input("Enter Employee ID: ").strip()
    try:
        new_salary = float(input("Enter New Salary: ").strip())
    except ValueError:
        print("Invalid salary.")
        return

    updated = False
    lines = []
    # I’ll read all records and update the one that matches
    with open(EMPLOYEE_FILE, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if parts[0] == emp_id:
                parts[3] = str(new_salary)
                updated = True
            lines.append(','.join(parts))

    # Rewrite the file with updated salary
    if updated:
        with open(EMPLOYEE_FILE, 'w') as f:
            for line in lines:
                f.write(line + '\n')
        print("Salary updated successfully!")
    else:
        print("Employee not found.")

# Function to generate department-wise report
def generate_report():
    summary = {}
    if not os.path.exists(EMPLOYEE_FILE):
        print("No employee records found.")
        return

    # Summarize salaries by department
    with open(EMPLOYEE_FILE, 'r') as f:
        for line in f:
            _, _, dept, salary, _ = line.strip().split(',')
            salary = float(salary)
            if dept not in summary:
                summary[dept] = {'count': 0, 'total': 0}
            summary[dept]['count'] += 1
            summary[dept]['total'] += salary

    # Write the report file
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        for dept, data in summary.items():
            avg = data['total'] / data['count']
            f.write(f"{dept} Department -> Employees: {data['count']} | Total Salary: {data['total']} | Average Salary: {avg:.1f}\n")

    print("Report generated successfully!")

# Function to delete employee record
def delete_employee():
    emp_id = input("Enter Employee ID to delete: ").strip()
    deleted = False
    lines = []
    # Keep all records except the one to delete
    with open(EMPLOYEE_FILE, 'r') as f:
        for line in f:
            if not line.startswith(emp_id + ','):
                lines.append(line.strip())
            else:
                deleted = True

    # Rewrite file without deleted employee
    if deleted:
        with open(EMPLOYEE_FILE, 'w') as f:
            for line in lines:
                f.write(line + '\n')
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")

# Main menu loop
def main():
    while True:
        print("\n==== Employee Record Management ====")
        print("1. Add New Employee")
        print("2. Display All Employees")
        print("3. Search Employee by ID")
        print("4. Update Employee Salary")
        print("5. Generate Department Report")
        print("6. Delete Employee")
        print("7. Exit")
        choice = input("Enter your choice: ").strip()

        # Based on choice, call respective function
        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_salary()
        elif choice == '5':
            generate_report()
        elif choice == '6':
            delete_employee()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

# Entry point
if __name__ == "__main__":
    main()


# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees     
# 3. Search Employee by ID     
# 4. Update Employee Salary    
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 2
# No employee records found.

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 1
# Enter Employee ID: E101
# Enter Name: Bhargavi S
# Enter Department: IT
# Enter Salary: 50000
# Enter Joining Date (YYYY-MM-DD): 2021-11-02
# Employee added successfully!

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 1
# Enter Employee ID: E103
# Enter Name: Meena
# Enter Department: Fianace
# Enter Salary: 60000
# Enter Joining Date (YYYY-MM-DD): 2021-02-04
# Employee added successfully!

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 1
# Enter Employee ID: E103
# Employee ID already exists.

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: E104
# Invalid choice. Try again.

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 1
# Enter Employee ID: E103
# Employee ID already exists.

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 1
# Enter Employee ID: E104
# Enter Name: Swathi
# Enter Department: Health
# Enter Salary: 67000
# Enter Joining Date (YYYY-MM-DD): 2019-06-04
# Employee added successfully!

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 1
# Enter Employee ID: E105
# Enter Name: Yashu
# Enter Department: HR
# Enter Salary: 8000
# Enter Joining Date (YYYY-MM-DD): 2016-03-02
# Employee added successfully!

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 1
# Enter Employee ID: E106
# Enter Name: Varsha
# Enter Department: HR
# Enter Salary: 45000
# Enter Joining Date (YYYY-MM-DD): 2015-03-02
# Employee added successfully!

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 2
# Employee Records:
# E101 | Bhargavi S | IT | 50000.0 | 2021-11-02
# E103 | Meena | Fianace | 60000.0 | 2021-02-04
# E104 | Swathi | Health | 67000.0 | 2019-06-04
# E105 | Yashu | HR | 8000.0 | 2016-03-02
# E106 | Varsha | HR | 45000.0 | 2015-03-02

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 3
# Enter Employee ID to search: E104
# Employee Found:
# E104 | Swathi | Health | 67000.0 | 2019-06-04

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 4
# Enter Employee ID: E101
# Enter New Salary: 45900
# Salary updated successfully!

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 5
# Report generated successfully!

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 6
# Enter Employee ID to delete: E104
# Employee deleted successfully!

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 7
# Exiting program.