#HR employee management System:

import os
from datetime import datetime

with open("employees.txt", "w") as file:
    file.write("E101,Neha Sharma,HR,60000,2020-05-10\n")
    file.write("E102,Ravi Kumar,IT,75000,2019-08-21\n")
    file.write("E103,Arjun Mehta,Finance,55000,2021-03-15\n")
    file.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
    file.write("E105,Vikram Singh,Operations,58000,2022-01-11\n")
    
#Add New Employee
with open("employees.txt", "a") as file:
    file.write("E106,Meera Nair,HR,64000,2022-11-20\n")

#Display All Employees
if not os.path.exists("employees.txt") or os.path.getsize("employees.txt") == 0:
    print("No employee records found.")
else:
    print("Employee Records:")
    with open("employees.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            print(" | ".join(parts))
            
#Search Employee by ID     
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


#updating the salary 
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

#generating the department wise data in report
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

#delete an employee
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
    print("Employee Not Found")

#output
# PS C:\Users\Administrator\day5_training> & "C:/Program Files/Python314/python.exe" c:/Users/Administrator/day5_training/task1_hr_employee_management_system.py
# Employee Records:
# E101 | Neha Sharma | HR | 60000 | 2020-05-10
# E102 | Ravi Kumar | IT | 75000 | 2019-08-21
# E103 | Arjun Mehta | Finance | 55000 | 2021-03-15    
# E104 | Fatima Khan | HR | 62000 | 2018-12-05
# E105 | Vikram Singh | Operations | 58000 | 2022-01-11
# E106 | Meera Nair | HR | 64000 | 2022-11-20
# Enter Employee ID to search: E104
# Employee Found:
# E104 | Fatima Khan | HR | 62000 | 2018-12-05
# Enter Employee ID: E104
# Enter New Salary: 65000
# Salary updated successfully!

# Report generated successfully

# Enter Employee ID to delete: E102
# Employee deleted successfully
# PS C:\Users\Administrator\day5_training> 