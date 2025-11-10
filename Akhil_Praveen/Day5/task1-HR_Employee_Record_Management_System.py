# HR_Employee_Record_Management_System

import os
def add_emp_details():
    emp_id = input("Enter Employee ID: ")
    with open("employee.txt","r") as file:
        line = file.readlines()
        for i in range(len(line)):
            if  line[i].startswith(emp_id):
                print("Employee is already exists!")
                return -1
    Name = input("Enter Name: ")
    dept = input("Enter Department: ")
    sal = int(input("Enter Salary:  "))
    join_date = input("Enter Joining Date (YYYY-MM-DD): ")
    
    with open("employee.txt","a") as file:
        file.write(f"{emp_id},{Name},{dept},{sal},{join_date}\n")
        print("Employee details added successfully!")

def display():
    with open("employee.txt","r") as file:
        line = file.readlines()
        for i in range(len(line)):
            print(f"line {i+1}:",line[i].strip())

def search():
    emp_id = input("Enter Employee ID: ")
    with open("employee.txt","r") as file:
        line = file.readlines()
        for i in range(len(line)):
            if  line[i].startswith(emp_id):
                print(f"Employee found:\n{line[i].strip()}") 
                return
        print("Employee not found")

def update_emp_sal():
    emp_id = input("Enter Employee ID: ")
    sal = input("Enter new salary: ")
    f=0
    with open("employee.txt","r+") as file:
        line = file.readlines()
        f=0
        for i in range(len(line)):
            if line[i].startswith(emp_id):
                detail= line[i].split(",")
                detail[3]=sal
                print(detail)
                file.seek(0)
                line[i] = ",".join(detail)
                file.writelines(line)
                print(f"Employee found:\n{line[i].strip()}")
                print("Salary changed successfully") 
                return
        print("Employee not found.")
    
    
def gen_dept_summary():
    dict={}
    with open("employee.txt","r") as file:
        line = file.readlines()
        for i in range(len(line)):
            dept = line[i].split(",")[2]
            if dept in dict:
                dict[dept][0] = dict[dept][0]+1
                dict[dept][1] +=int(line[i].split(",")[3])
            else:
                dict[dept]=[1,int(line[i].split(",")[3])]
    for i in dict:
        sal = dict[i][1]
        count=dict[i][0]
        dict[i].append(sal/count)
    with open("report.txt","w",encoding="utf-8") as report:
        line = []
        for i in dict:
            sal = dict[i][1]
            count=dict[i][0]
            avg = dict[i][2]
            line.append(f"{i} Department -> Employees: {count} | Total Salary: {sal} | Average Salary: {avg} \n")
        report.writelines(line)
    
    with open("report.txt","r") as report: 
        print(report.read())

def delete_emp_rec():
    
    emp_id = input("Enter Employee ID: ")
    with open("employee.txt","r+") as file:
        line = file.readlines()
        ind=0
        f=0
        for i in range(len(line)):
            if line[i].startswith(emp_id):
                ind=i
                print("Employee details deleted successfully.")
                f=1
                break
        if f==1:
            new_line = line[:ind]+line[ind+1:]
            file.seek(0)
            file.writelines(new_line)
            file.truncate()
        else:
            print("Employee doesn't Exists!")

print("=====   Corporate Skill Matrix System =====")
print("1. Add New Employee")
print("2. Display All Employees")
print("3. Search Employee by ID")
print("4. Update Employee Salary")
print("5. Generate Department-wise Summary Reportl")
print("6. Delete Employee Record")

while True:
    choice = int(input("Enter your choice: "))
    if(choice==1):
        add_emp_details()
    elif(choice==2):
        display()
    elif(choice==3):
        search()
    elif(choice==4):
        update_emp_sal()
    elif(choice==5):
        gen_dept_summary()
    elif(choice==6):
        delete_emp_rec()
    elif(choice==7):
        print("Thank you!")
        break
    else:
        print("Invalid choice please enter valid choice.")
    print("")
    
# Sample output
# =====   Corporate Skill Matrix System =====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department-wise Summary Reportl
# 6. Delete Employee Record
# Enter your choice: 1
# Enter Employee ID: E101
# Employee is already exists!

# Enter your choice: 1
# Enter Employee ID: E107
# Enter Name: Akhil praveen
# Enter Department: IT
# Enter Salary:  100000
# Enter Joining Date (YYYY-MM-DD): 2025-11-03
# Employee details added successfully!

# Enter your choice: 2
# line 1: E101,Neha Sharma,HR,60000,2020-05-10
# line 2: E102,Ravi Kumar,IT,75000,2019-08-21
# line 3: E103,Arjun Mehta,Finance,55000,2021-03-15
# line 4: E104,Fatima Khan,HR,62000,2018-12-05
# line 5: E105,Vikram Singh,Operations,58000,2022-01-11
# line 6: E107,Akhil praveen,IT,100000,2025-11-03

# Enter your choice: 3
# Enter Employee ID: E107
# Employee found:
# E107,Akhil praveen,IT,100000,2025-11-03

# Enter your choice: 4
# Enter Employee ID: E107
# Enter new salary: 150000
# ['E107', 'Akhil praveen', 'IT', '150000', '2025-11-03\n']
# Employee found:
# E107,Akhil praveen,IT,150000,2025-11-03
# Salary changed successfully

# Enter your choice: 2
# line 1: E101,Neha Sharma,HR,60000,2020-05-10
# line 2: E102,Ravi Kumar,IT,75000,2019-08-21
# line 3: E103,Arjun Mehta,Finance,55000,2021-03-15
# line 4: E104,Fatima Khan,HR,62000,2018-12-05
# line 5: E105,Vikram Singh,Operations,58000,2022-01-11
# line 6: E107,Akhil praveen,IT,150000,2025-11-03

# Enter your choice: 5
# HR Department -> Employees: 2 | Total Salary: 122000 | Average Salary: 61000.0 
# IT Department -> Employees: 2 | Total Salary: 225000 | Average Salary: 112500.0
# Finance Department -> Employees: 1 | Total Salary: 55000 | Average Salary: 55000.0
# Operations Department -> Employees: 1 | Total Salary: 58000 | Average Salary: 58000.0


# Enter your choice: 6
# Enter Employee ID: E107
# Employee details deleted successfully.

# Enter your choice: 2
# line 1: E101,Neha Sharma,HR,60000,2020-05-10
# line 2: E102,Ravi Kumar,IT,75000,2019-08-21
# line 3: E103,Arjun Mehta,Finance,55000,2021-03-15
# line 4: E104,Fatima Khan,HR,62000,2018-12-05
# line 5: E105,Vikram Singh,Operations,58000,2022-01-11

# Enter your choice: 7
# Thank you!