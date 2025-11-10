# HR Employee Record Management
# System
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
# Functional Requirements
# Your program must provide the following 6 major operations.
# Each operation should be implemented as a separate function.
# ��Add New Employee
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
# ��Display All Employees
# Read and print all records neatly formatted.
# Handle case when the file is empty.
# Example output:
# Employee Records:
# E101 | Neha Sharma | HR | 60000 | 2020-05-10
# E102 | Ravi Kumar | IT | 75000 | 2019-08-21
# ...
# ��Search Employee by ID
# Ask the user for an Employee ID.
# Search the file line by line.
# If found, display the employee details.
# If not found, print a message “Employee not found.”
# Example:
# Enter Employee ID to search: E103
# Employee Found:
# E103 | Arjun Mehta | Finance | 55000 | 2021-03-15
# ��Update Employee Salary
# Text File Task 3
# Ask for Employee ID and new salary.
# Read all lines, modify the correct line, and rewrite the file with the updated
# data.
# Example:
# Enter Employee ID: E104
# Enter New Salary: 65000
# Result:
# E104,Fatima Khan,HR,65000,2018-12-05
# ��Generate Department-wise Summary Report
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
# ��Delete Employee Record
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
# Expected Structure
# employee_management.py
# employees.txt
# report.txt
# Example Output Snapshot
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# Text File Task 5
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 2
# Employee Records:
# E101 | Neha Sharma | HR | 60000 | 2020-05-10
# E102 | Ravi Kumar | IT | 75000 | 2019-08-21
# E103 | Arjun Mehta | Finance | 55000 | 2021-03-15
# E104 | Fatima Khan | HR | 62000 | 2018-12-05
# E105 | Vikram Singh | Operations | 58000 | 2022-01-11
# Enhancement
# If participants finish early, suggest these improvements:
# Add option to export report with date in filename, e.g., report_2025-11-10.txt
# Add input validation (e.g., salary must be a number)
# Add a feature to list employees joined before 2020
# Add error handling (try/except) if file not found
import os
from datetime import datetime

EMPLOYEE_FILE = "employees.txt"
REPORT_FILE = f"report_{datetime.now().strftime('%Y-%m-%d')}.txt"


if not os.path.exists(EMPLOYEE_FILE):
    with open(EMPLOYEE_FILE, "w") as f:
        f.write("E101,Neha Sharma,HR,60000,2020-05-10\n"
                "E102,Ravi Kumar,IT,75000,2019-08-21\n"
                "E103,Arjun Mehta,Finance,55000,2021-03-15\n"
                "E104,Fatima Khan,HR,62000,2018-12-05\n"
                "E105,Vikram Singh,Operations,58000,2022-01-11\n")

def load_employees():
    with open(EMPLOYEE_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_employees(employees):
    with open(EMPLOYEE_FILE, "w") as f:
        f.write("\n".join(employees) + "\n")

def add_employee():
    employees = load_employees()
    emp_ids = [e.split(",")[0] for e in employees]

    emp_id = input("Enter Employee ID: ").strip()
    if emp_id in emp_ids:
        print("Employee ID already exists.")
        return

    name = input("Enter Name: ").strip()
    dept = input("Enter Department: ").strip()
    try:
        salary = int(input("Enter Salary: ").strip())
    except ValueError:
        print("Invalid salary.")
        return
    join_date = input("Enter Joining Date (YYYY-MM-DD): ").strip()

    new_record = f"{emp_id},{name},{dept},{salary},{join_date}"
    with open(EMPLOYEE_FILE, "a") as f:
        f.write(new_record + "\n")
    print("Employee added successfully!")

def display_employees():
    employees = load_employees()
    if not employees:
        print("No employee records found.")
        return
    print("\nEmployee Records:")
    for e in employees:
        print(" | ".join(e.split(",")))

def search_employee():
    emp_id = input("Enter Employee ID to search: ").strip()
    employees = load_employees()
    for e in employees:
        if e.startswith(emp_id):
            print("Employee Found:")
            print(" | ".join(e.split(",")))
            return
    print("Employee not found.")

def update_salary():
    emp_id = input("Enter Employee ID: ").strip()
    try:
        new_salary = int(input("Enter New Salary: ").strip())
    except ValueError:
        print("Invalid salary.")
        return

    employees = load_employees()
    updated = False
    for i, e in enumerate(employees):
        parts = e.split(",")
        if parts[0] == emp_id:
            parts[3] = str(new_salary)
            employees[i] = ",".join(parts)
            updated = True
            break

    if updated:
        save_employees(employees)
        print("Salary updated successfully!")
    else:
        print("Employee not found.")

def generate_report():
    employees = load_employees()
    summary = {}
    for e in employees:
        parts = e.split(",")
        dept = parts[2]
        salary = int(parts[3])
        if dept not in summary:
            summary[dept] = {"count": 0, "total": 0}
        summary[dept]["count"] += 1
        summary[dept]["total"] += salary

    with open(REPORT_FILE, "w") as f:
        for dept, data in summary.items():
            avg = data["total"] / data["count"]
            line = f"{dept} Department → Employees: {data['count']} | Total Salary: {data['total']} | Average Salary: {avg:.2f}"
            f.write(line + "\n")
            print(line)
    print(f"\nReport saved to {REPORT_FILE}")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ").strip()
    employees = load_employees()
    new_employees = [e for e in employees if not e.startswith(emp_id)]
    if len(new_employees) == len(employees):
        print("Employee not found.")
    else:
        save_employees(new_employees)
        print("Employee deleted successfully!")
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
        print("Invalid choice. Please try again.")
        
# sample output
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
# E101 | Neha Sharma | HR | 60000 | 2020-05-10
# E102 | Ravi Kumar | IT | 75000 | 2019-08-21
# E103 | Arjun Mehta | Finance | 55000 | 2021-03-15
# E104 | Fatima Khan | HR | 62000 | 2018-12-05
# E105 | Vikram Singh | Operations | 58000 | 2022-01-11

# ==== Employee Record Management ====
# Enter your choice: 3
# Enter Employee ID to search: E103
# Employee Found:
# E103 | Arjun Mehta | Finance | 55000 | 2021-03-15

# ==== Employee Record Management ====
# Enter your choice: 4
# Enter Employee ID: E104
# Enter New Salary: 65000
# Salary updated successfully!

# ==== Employee Record Management ====
# Enter your choice: 5
# HR Department → Employees: 2 | Total Salary: 125000 | Average Salary: 62500.00
# IT Department → Employees: 1 | Total Salary: 75000 | Average Salary: 75000.00
# Finance Department → Employees: 1 | Total Salary: 55000 | Average Salary: 55000.00
# Operations Department → Employees: 1 | Total Salary: 58000 | Average Salary: 58000.00

# Report saved to report_2025-11-10.txt

# ==== Employee Record Management ====
# Enter your choice: 6
# Enter Employee ID to delete: E105
# Employee deleted successfully!

# ==== Employee Record Management ====
# Enter your choice: 7
# Exiting program.
