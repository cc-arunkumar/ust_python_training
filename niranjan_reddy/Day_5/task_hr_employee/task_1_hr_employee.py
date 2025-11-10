
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



from ntpath import join
import os


# Add New Employee

with open("employees.txt","w") as file:
    file.write("E101,Neha Sharma,HR,60000,2020-05-10\n")
    file.write("E102,Ravi Kumar,IT,75000,2019-08-21\n")
    file.write("E103,Arjun Mehta,Finance,55000,2021-03-15\n")
    file.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
    file.write("E105,Vikram Singh,Operations,58000,2022-01-11\n")
    
emp_id=input("Enter Employee ID:")
name=input("Enter Name:")
depatment_name=input("Enter Department:")
salary=input("Enter Salary:")
date=input("Enter Joining Date (YYYY-MM-DD):")

new_record=emp_id+","+name+","+depatment_name+","+salary+","+date
flag=False
with open("employees.txt","r") as file:
    for line in file:
        existing=line.strip().split(",")[0]
        if existing==emp_id:
            flag=True
            break

if flag:
    print("File already exists")
else:
    print("File doesn't exists")


# Display All Employees    
    
with open("employees.txt","a") as file:
    file.write("E106,Meera Nair,HR,64000,2022-11-20")


# Search Employee by ID

with open("employees.txt","r") as file:
    content=file.read().splitlines()
    for line in content:
        data=line.split(",")
        print("|".join(data))
emp_id=input("Enter Employee ID to search:")

flag=False
with open ("employees.txt","r") as file:
    line=file.read().split(",")
    for line in file:
        lines=line.split(",")
        if lines[0]==emp_id:
            print(f"{line[0]}, {line[1]}, {line[2]} , {line[3]}, {line[4]}")
            flag=True
            break
if not flag:
    print("Employee not found")   
    
    
# Update Employee Salary
 
emp_id=input("Enter Employee ID:")
sal=float(input("Enter New Salary:"))
        
data=[]
with open("employees.txt","r") as file:
    for line in file:
        lines=line.strip().split(",")
        if lines[0]==emp_id:
            lines[3]=str(sal)
            data.append(",".join(data))
with open("employees.txt","w") as file:
    for line in data:
        file.write(line+"\n")
        
        
        
# Generate Department-wise Summary Report

dict={}
data=[]
with open("employees.txt","r") as file:
    for line in file:
        lines=line.strip().split(",")
        emp_id,name,dept,salary,date=lines
        data.append(lines)
        salary=float(salary)
        
        if dept not in data:
            dict[dept]={"count":0,"total":0}
        dict[dept]["count"]+=1
        dict[dept]["total"]+=salary
        
        
with open("reports.txt","w") as report:
    for dept,val in dict.items():
        count=val["count"]
        total=val["total"]
        average=total/count
        
        report_line=f"{dept} Department -> Employees: {count} | Total Salary: {total} | Average salary: {average:.1f}\n "
        report.write(report_line)        
 
 
 
 
# Delete Employee Record       

emp_id="E104"

with open("employees.txt","r") as file:
    lines=file.readlines()
    
flag=False

with open("employees.txt","w") as file:
    for line in lines:
        if line.startswith(emp_id+","):
            flag=True
            continue
        file.write(line)
if flag:
    print("Employee deleted successfully!")
else:
    print("Employee Not found")
      
      
      
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

print("==== Employee Record Management ====")
print("1. Add New Employee")
print("2. Display All Employees")
print("3. Search Employee by ID")
print("4. Update Employee Salary")
print("5. Generate Department Report")
print("6. Delete Employee")
print("7. Exit")

choice=int(input("Enter your choice:"))
while(choice<8):
    
    if choice ==1:
        emp_id=input("Enter Employee ID:")
        name=input("Enter Name:")
        depatment_name=input("Enter Department:")
        salary=input("Enter Salary:")
        date=input("Enter Joining Date (YYYY-MM-DD):")

        new_record=emp_id+","+name+","+depatment_name+","+salary+","+date
            
        with open("employees.txt","a") as file:
            file.write(new_record)
        flag=False
        with open("employees.txt","r") as file:
            for line in file:
                existing=line.strip().split(",")[0]
                if existing==emp_id:
                    flag=True
                    break

        if flag:
            print("File already exists")
        else:
            print("File Not Found")
                
    elif choice==2:
        with open("employees.txt","r") as file:
            content=file.read()
            print(content)
    elif choice==3:
        
        emp_id=input("Enter Employee ID to search:")
        flag=False
        with open ("employees.txt","r") as file:
            for line in file:
                lines=line.strip()
                parts=line.split(",")
                if parts[0]==emp_id:
                    print(f"{parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]}")
                    flag=True
                    break
        if not flag:
            print("Employee not found")
            
    elif choice==4:
        emp_id=input("Enter Employee ID:")
        sal=float(input("Enter New Salary:"))
        
        data=[]
        with open("employees.txt","r") as file:
            for line in file:
                lines=line.strip().split(",")
                if lines[0]==emp_id:
                    lines[3]=str(sal)
                data.append(",".join(data))
        with open("employees.txt","w") as file:
            for line in data:
                file.write(line+"\n")
                
    elif choice==5:
        dict={}
        data=[]
        with open("employees.txt","r") as file:
            for line in file:
                lines=line.strip().split(",")
                emp_id,name,dept,salary,date=lines
                data.append(lines)
                salary=float(salary)
                
                if dept not in data:
                    dict[dept]={"count":0,"total":0}
                dict[dept]["count"]+=1
                dict[dept]["total"]+=salary
                
                
        with open("reports.txt","w") as report:
            for dept,val in dict.items():
                count=val["count"]
                total=val["total"]
                average=total/count
                
                report_line=f"{dept} Department -> Employees: {count} | Total Salary: {total} | Average salary: {average:.1f}\n "
                report.write(report_line)
        
    elif choice==6:
        emp_id=input("Enter Employee ID to delete:")
        with open("employees.txt","r") as file:
            lines=file.readlines()
            
        flag=False

        with open("employees.txt","w") as file:
            for line in lines:
                if line.startswith(emp_id+","):
                    flag=True
                    continue
                file.write(line)
        if flag:
            print("Employee deleted successfully!")
        else:
            
            print("Employee Not found")
            
    elif choice==7:
        print("Thank You! Successfully exited")
        break
    choice=int(input("Enter your choice: "))


# Sample Output
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees     
# 3. Search Employee by ID     
# 4. Update Employee Salary    
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit

# Enter your choice:2
# E101,Neha Sharma,HR,60000,2020-05-10
# E102,Ravi Kumar,IT,75000,2019-08-21
# E103,Arjun Mehta,Finance,55000,2021-03-15    
# E104,Fatima Khan,HR,62000,2018-12-05
# E105,Vikram Singh,Operations,58000,2022-01-11

# Enter your choice: 3
# Enter Employee ID to search:E104
# E104 | Fatima Khan | HR | 62000 | 2018-12-05

# Enter your choice: 5

# Enter your choice: 7
# Thank You! Successfully exited