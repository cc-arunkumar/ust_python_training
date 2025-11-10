"""
HR Employee Record Management
System
Objective
Design a simple Python file handling program that manages employee
information using .txt files.
The program should allow adding, reading, searching, updating, and summarizing
employee records — all stored in plain text format.
Participants will build this system from scratch, practicing all file operations ( read ,
write , append , seek , etc.) while maintaining data consistency
"""


import os
from datetime import datetime

EMP_FILE="DAY 5/files/employe.txt"

def add_employee():
    id=input("Enter Employee ID : ")

    name=input("Enter Employee Name : ")
    department=input("Enter Deparment Name : ")
    salary=input("Enter Salary : ")
    doj=input("Enter Date (YYYY-MM-DD):")

    with open(EMP_FILE,"a") as f:
        f.write(f"{id},{name},{department},{salary},{doj}\n")
        
    print("File Added Sucessfully")

def display():
    with open(EMP_FILE,"r") as f:
        content=f.read()
        print(content)

def search():
    id_to_find=input("Enter Employee ID to search :")
    with open(EMP_FILE,"r") as f:
        for line in f:
            if line.startswith(id_to_find+","):
                id,name,dep, salary,doj= line.strip().split(",")
                print("The EMployee Details")
                print(f"{id} | {name} | {salary} | {doj}")
                break


def delete_emp():
    emp_id=input("Enter Employee ID to delete :")
    found=False

    with open(EMP_FILE,"r") as f:
        lines=f.readlines()

    with open(EMP_FILE,"w") as f:
        for line in lines:
            if not line.startswith(emp_id+","):
                f.write(line)
            else: found=True
    
    if found: print("Deleted sucessfully")
    else: print("Employee not Found")

def updated_salary():
    up_id=input("Enter Employee ID :")
    up_sal=int(input("Enter Updated Salary :"))
    found=False

    with open(EMP_FILE,"r") as f:
        lines=f.readlines()
    
    with open(EMP_FILE,"w") as f:
        for line in lines:
            if line.startswith(up_id+","):
                parts=line.strip().split(",")
                parts[3]=str(up_sal)
                line=",".join(parts)+"\n"
                found=True
            f.write(line)

    if found:
        print("Salary Updated Sucessfully")
    else: print("No employees FOund")

def generate_rep():
    if not os.path.exists(EMP_FILE) or os.path.getsize(EMP_FILE)==0:
        print("No employee data available to generate report.")
        return

    dept_data={}

    with open(EMP_FILE,"r") as f:
        for line in f:
            id,name,dep,salary,doj=line.strip().split(",")
            salary=int(salary)
            if dep not in dept_data:
                dept_data[dep]={"count":0,"total":0}
            dept_data[dep]["count"]+=1
            dept_data[dep]["total"]+=salary

    rep_path="DAY 5/files/report.txt"
    with open(rep_path,"w",encoding="utf-8") as r:
        for dep,info in dept_data.items():
            count=info["count"]
            total=info["total"]
            avg=total/count
            r.write(f"{dep} Department → Employees: {count} | Total Salary: {total} | Average Salary: {avg:.1f}\n")

    print("report generated successfully in report.txt")




while True:
    print("Enter Your Choicees")
    print("1. Add Employee")
    print("2, Display EMployee")
    print("3, Search by ID")
    print("4, Update Employee Salary")
    print("5, Report")
    print("6, Delete Employee")
    print("7, Exit")
    choice=int(input("Enter the Choice :"))

    if choice==1:
        add_employee()
    elif choice==2:
        display()
    elif choice==3:
        search()
    elif choice==4:
        updated_salary()
    elif choice==5:
        generate_rep()
    elif choice==6:
        delete_emp()
    else:
        print("Thanks for Using !!!")
        break

"""
SAMPLE OUTPUT

Enter Your Choicees
1. Add Employee
2, Display EMployee
3, Search by ID
4, Update Employee Salary
5, Report
6, Delete Employee
7, Exit
Enter the Choice :1
Enter Employee ID : 1
Enter Employee Name : Gowtham
Enter Deparment Name : IT
Enter Salary : 40000
Enter Date (YYYY-MM-DD):2025-01-01
File Added Sucessfully
Enter Your Choicees
1. Add Employee
2, Display EMployee
3, Search by ID
4, Update Employee Salary
5, Report
6, Delete Employee
7, Exit
Enter the Choice :1
Enter Employee ID : 2
Enter Employee Name : Mani
Enter Deparment Name : R/D
Enter Salary : 50000
Enter Date (YYYY-MM-DD):2025-10-10
File Added Sucessfully
Enter Your Choicees
1. Add Employee
2, Display EMployee
3, Search by ID
4, Update Employee Salary
5, Report
6, Delete Employee
7, Exit
Enter the Choice :2
1,Gowtham,IT,40000,2025-01-01
2,Mani,R/D,50000,2025-10-10

Enter Your Choicees
1. Add Employee
2, Display EMployee
3, Search by ID
4, Update Employee Salary
5, Report
6, Delete Employee
7, Exit
Enter the Choice :3
Enter Employee ID to search :2
The EMployee Details
2 | Mani | 50000 | 2025-10-10
Enter Your Choicees
1. Add Employee
2, Display EMployee
3, Search by ID
4, Update Employee Salary
5, Report
6, Delete Employee
7, Exit
Enter the Choice :4
Enter Employee ID :1
Enter Updated Salary :60000
Salary Updated Sucessfully
Enter Your Choicees
1. Add Employee
2, Display EMployee
3, Search by ID
4, Update Employee Salary
5, Report
6, Delete Employee
7, Exit
Enter the Choice :5
report generated successfully in report.txt
Enter Your Choicees
1. Add Employee
2, Display EMployee
3, Search by ID
4, Update Employee Salary
5, Report
6, Delete Employee
7, Exit
Enter the Choice :6
Enter Employee ID to delete :2
Deleted sucessfully
Enter Your Choicees
1. Add Employee
2, Display EMployee
3, Search by ID
4, Update Employee Salary
5, Report
6, Delete Employee
7, Exit
Enter the Choice :7
Thanks for Using !!!

"""