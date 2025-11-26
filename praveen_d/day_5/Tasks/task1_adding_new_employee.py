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


import os

with open("employess.txt","w") as file:

    file.write("E101,Neha Sharma,HR,60000,2020-05-10\n")
    file.write("E102,Ravi Kumar,IT,75000,2019-08-21\n")
    file.write("E103,Arjun Mehta,Finance,55000,2021-03-15\n")
    file.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
    file.write("E105,Vikram Singh,Operations,58000,2022-01-11")

emp_ids = []
if os.path.exists("employess.txt"):
    with open("employess.txt","r") as file:
        for line in file:
            line_one = line.strip().split(",")
            if line_one and line_one[0]:
                emp_ids.append(line_one[0])

def append_info():
    employee_id=input("Enter Employee ID:")
    employee_name=input("Enter employee name:")
    employee_dept=input("Enter department:")
    employee_salary=input("Enter salary:")
    employee_joining_date=input("Enter Joining date(YYYY-MM-DD):")

    if employee_id not in emp_ids:
        write_prefix = "\n" if os.path.exists("employess.txt") and os.path.getsize("employess.txt") > 0 else ""
        with open("employess.txt","a") as file:
            file.write(f"{write_prefix}{employee_id},{employee_name},{employee_dept},{employee_salary},{employee_joining_date}")
            print("Appended sucessfully")
        emp_ids.append(employee_id)
    else:
        print("Employee ID already exists")

def display_info():
    if os.path.exists("employess.txt"):
        with open("employess.txt","r") as file:
            context= file.read()
            print(context)
    else:
        print("The file not found")

def search_user():
     emp_id= input("Enter employee id you want to search:")
     is_found=False
     if not os.path.exists("employess.txt"):
         print("The file not found")
         return
     with open("employess.txt","r") as file:
          for line in file:
               info= line.strip().split(",")
               if info and info[0] ==emp_id:
                    print(info)
                    is_found=True
     if is_found==False:
          print("The employee id not found")

def update_salary():
     emp_id=input("Enter employee id:")
     updated_salary=input("Enter the updated salary:")

     if os.path.exists("employess.txt"):
        with open("employess.txt","r") as file:
               copy_list=file.readlines()
        
        with open("employess.txt","w") as file:
              for line in copy_list:
                    each_line=line.strip().split(",")
                    if each_line and each_line[0]==emp_id:
                         if len(each_line)>=4:
                              each_line[3]=updated_salary
                         file.write(",".join(each_line)+"\n")
                    else:
                         file.write(line)

        with open("employess.txt","r") as file:
             context=file.read()
             print(context)
     else:
         print("The file not found")

def generate_dept_wise_report():
     HR_dept=0
     HR_salary=0
     IT_dept=0
     IT_salary=0
     finance_dept=0
     finance_salary=0
     operations_dept=0
     operations_salary=0
     if not os.path.exists("employess.txt"):
         print("The file not found")
         return
     with open("employess.txt","r") as file:
          for line in file:
            each_line=line.strip().split(",")
            if len(each_line)<4:
                continue
            dept=each_line[2]
            try:
                sal=int(each_line[3])
            except ValueError:
                continue
            if dept=="HR":
                    HR_dept+=1
                    HR_salary+=sal
            elif dept=="IT":
                IT_dept+=1
                IT_salary+=sal
            elif dept=="Finance":
                 finance_dept+=1
                 finance_salary+=sal
            else:
                 operations_dept+=1
                 operations_salary+=sal

     with open("report.txt","w") as file:
        if HR_dept:
            file.write(f"HR Department->Employess:{HR_dept} | Total Salary:{HR_salary} | Average Salary:{HR_salary/HR_dept}\n")
        else:
            file.write("HR Department->Employess:0 | Total Salary:0 | Average Salary:0\n")

        if IT_dept:
            file.write(f"IT Department -> Employees:{IT_dept}| Total Salary: {IT_salary} | Average Salary: {IT_salary/IT_dept}\n")
        else:
            file.write("IT Department -> Employees:0| Total Salary: 0 | Average Salary: 0\n")

        if finance_dept:
            file.write(f"Finance Department -> Employees:{finance_dept} | Total Salary:{finance_salary} | Average Salary:{finance_salary/finance_dept}\n")
        else:
            file.write("Finance Department -> Employees:0 | Total Salary:0 | Average Salary: 0\n")

        if operations_dept:
            file.write(f"Operations Department -> Employees:{operations_dept} | Total Salary:{operations_salary} | Average Salary:{operations_salary/operations_dept}")
        else:
            file.write("Operations Department -> Employees:0 | Total Salary:0 | Average Salary: 0")
        print("The report file writted sucessfully")         

def delete_employee_record():
     emp_id=input("Get emp id:")
     if not os.path.exists("employess.txt"):
         print("The file not found")
         return

     with open("employess.txt","r") as file:
          copy_record=file.readlines()
          print("OLD RECORD:")
          print(copy_record)

     found=False
     for line in copy_record:
          parts=line.strip().split(",")
          if parts and parts[0]==emp_id:
               found=True
               break

     if not found:
          print(f"Employee id {emp_id} not found; nothing removed.")
          return

     with open("employess.txt","w") as file:
          for line in copy_record:
               each_line =line.strip().split(",")
               if each_line and each_line[0]==emp_id:
                    print(f"removed:Employee:{emp_id}")
                    continue
               else:
                    file.write(line)

     with open("employess.txt","r") as file:
          new_record=file.readlines()
          print(new_record)
               
choose=True
while choose:
     print("1.Delete_employee_record")
     print("2.Generate_dept_wise_report")
     print("3.Update_salary")
     print("4.Search_user")
     print("5.Append_info")
     print("6.Display_info")
     print("7.Exit..........")

     option=int(input("Enter the option:"))
     match option:
          case 1:
               delete_employee_record()
          case 2:
               generate_dept_wise_report()
          case 3:
               update_salary()
          case 4:
               search_user()
          case 5:
               append_info()
          case 6:
               display_info()
          case 7:
               print("Exiting............")
               choose=False

# PS C:\UST python> & C:/Users/303489/AppData/Local/Programs/Python/Python312/python.exe "c:/UST python/Praveen D/Day 5/Tasks/task1_adding_new_employee.py"
# 1.Delete_employee_record
# 2.Generate_dept_wise_report
# 3.Update_salary
# 4.Search_user
# 5.Append_info
# 6.Display_info
# 7.Exit..........
# Enter the option:1
# Get emp id:E106
# OLD RECORD:
# ['E101,Neha Sharma,HR,60000,2020-05-10\n', 'E102,Ravi Kumar,IT,75000,2019-08-21\n', 'E103,Arjun Mehta,Finance,55000,2021-03-15\n', 'E104,Fatima Khan,HR,62000,2018-12-05\n', 'E105,Vikram Singh,Operations,58000,2022-01-11']
# Employee id E106 not found; nothing removed.
# 1.Delete_employee_record
# 2.Generate_dept_wise_report
# 3.Update_salary
# 4.Search_user
# 5.Append_info
# 6.Display_info
# 7.Exit..........
# Enter the option:1
# Get emp id:E102
# OLD RECORD:
# ['E101,Neha Sharma,HR,60000,2020-05-10\n', 'E102,Ravi Kumar,IT,75000,2019-08-21\n', 'E103,Arjun Mehta,Finance,55000,2021-03-15\n', 'E104,Fatima Khan,HR,62000,2018-12-05\n', 'E105,Vikram Singh,Operations,58000,2022-01-11']
# removed:Employee:E102
# ['E101,Neha Sharma,HR,60000,2020-05-10\n', 'E103,Arjun Mehta,Finance,55000,2021-03-15\n', 'E104,Fatima Khan,HR,62000,2018-12-05\n', 'E105,Vikram Singh,Operations,58000,2022-01-11']
# 1.Delete_employee_record
# 2.Generate_dept_wise_report
# 3.Update_salary
# 4.Search_user
# 5.Append_info
# 6.Display_info
# 7.Exit..........
# Enter the option:2
# The report file writted sucessfully
# 1.Delete_employee_record
# 2.Generate_dept_wise_report
# 3.Update_salary
# 4.Search_user
# 5.Append_info
# 6.Display_info
# 7.Exit..........
# Enter the option:3
# Enter employee id:104
# Enter the updated salary:65000
# E101,Neha Sharma,HR,60000,2020-05-10
# E103,Arjun Mehta,Finance,55000,2021-03-15
# E104,Fatima Khan,HR,62000,2018-12-05
# E105,Vikram Singh,Operations,58000,2022-01-11
# 1.Delete_employee_record
# 2.Generate_dept_wise_report
# 3.Update_salary
# 4.Search_user
# 5.Append_info
# 6.Display_info
# 7.Exit..........
# Enter the option:4
# Enter employee id you want to search:E101
# ['E101', 'Neha Sharma', 'HR', '60000', '2020-05-10']
# 1.Delete_employee_record
# 2.Generate_dept_wise_report
# 3.Update_salary
# 4.Search_user
# 5.Append_info
# 6.Display_info
# 7.Exit..........
# Enter the option:5
# Enter Employee ID:E106
# Enter employee name:Neha
# Enter department:HR
# Enter salary:70000
# Enter Joining date(YYYY-MM-DD):2025-05-21
# Appended sucessfully
# 1.Delete_employee_record
# 2.Generate_dept_wise_report
# 3.Update_salary
# 4.Search_user
# 5.Append_info
# 6.Display_info
# 7.Exit..........
# Enter the option:6
# E101,Neha Sharma,HR,60000,2020-05-10
# E103,Arjun Mehta,Finance,55000,2021-03-15
# E104,Fatima Khan,HR,62000,2018-12-05
# E105,Vikram Singh,Operations,58000,2022-01-11
# E106,Neha,HR,70000,2025-05-21
# 1.Delete_employee_record
# 2.Generate_dept_wise_report
# 3.Update_salary
# 4.Search_user
# 5.Append_info
# 6.Display_info
# 7.Exit..........
# Enter the option:7
# Exiting............
# PS C:\UST python> 