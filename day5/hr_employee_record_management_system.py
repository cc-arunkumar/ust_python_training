#hr employee management system
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
updated_lines=[]
with open("employees.txt", "r") as file:
    for line in file:
        parts=line.strip().split(",")
        if parts[0]==emp_id:
            parts[3]=new_salary  
        updated_lines.append(",".join(parts))
with open("employees.txt", "w") as file:
    for line in updated_lines:
        file.write(line + "\n")

print("Salary updated successfully!")

#employee report
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
emp_id = input("\nEnter Employee id to delete: ").strip()
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




#  output
#  Employee Records:
# E101 | Neha Sharma | HR | 60000 | 2020-05-10
# E102 | Ravi Kumar | IT | 75000 | 2019-08-21
# E103 | Arjun Mehta | Finance | 55000 | 2021-03-15    
# E104 | Fatima Khan | HR | 62000 | 2018-12-05
# E105 | Vikram Singh | Operations | 58000 | 2022-01-11
# E106 | Meera Nair | HR | 64000 | 2022-11-20
# Enter Employee ID to search: 104
# Employee not found.
# Enter Employee ID: E901
# Enter New Salary: 300000
# Salary updated successfully!

# Report generated successfully

# Enter Employee id to delete: E102
# Employee deleted successfully       