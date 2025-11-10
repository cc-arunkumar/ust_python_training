import os
import datetime
from search_emp import search_emp
from diplay_emp import dis_emp
from del_emp import delete_emp
from add_emp import add_emp
from report_emp import report
from update_emp import update_sal




with open("employees.txt","w") as file:
    file.write('''E101,Neha Sharma,HR,60000,2020-05-10
E102,Ravi Kumar,IT,75000,2019-08-21
E103,Arjun Mehta,Finance,55000,2021-03-15
E104,Fatima Khan,HR,62000,2018-12-05
E105,Vikram Singh,Operations,58000,2022-01-11''')
emp_unique=set()

with open("employees.txt","r") as file:
    for line in file:
        details=line.strip().split(",")
        emp_unique.add(details[0])


print("====HR Management Portal=====")
print('''1. Add New Employee
2. Display All Employees
3. Search Employee by ID
4. Update Employee Salary
5. Generate Department Report
6. Delete Employee
7. Exit
Enter your choice:
''')
choice=int(input())
while(choice>0 and choice<7):

    if (choice==1):
        add_emp()
    elif (choice==2):
        dis_emp()
    elif (choice==3):
        search_emp()
    elif (choice==4):
        update_sal()
    elif (choice==5):
        report()
    elif(choice==6):
        delete_emp()
    else:
        print("Thankyou,Exiting....")
        break
    choice=int(input("Enter choice"))



# add_emp()s
# search_emp()
# update_sal()

# content=open(employees.txt).read()
# print("employee details:\n",content)

# ====HR Management Portal=====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice:

# 1
# Enter Employee ID: E109
# Enter Employee Name: Arumukesh
# Enter Department: IT
# Enter Salary: 38000
# Enter Joining Date (YYYY-MM-DD): 2025-10-10
# employee details:
#  E101,Neha Sharma,HR,60000,2020-05-10
# E102,Ravi Kumar,IT,75000,2019-08-21
# E103,Arjun Mehta,Finance,55000,2021-03-15
# E104,Fatima Khan,HR,62000,2018-12-05
# E105,Vikram Singh,Operations,58000,2022-01-11
# E109,Arumukesh,IT,38000,2025-10-10
# Enter choice2
# E101,Neha Sharma,HR,60000,2020-05-10
# E102,Ravi Kumar,IT,75000,2019-08-21
# E103,Arjun Mehta,Finance,55000,2021-03-15
# E104,Fatima Khan,HR,62000,2018-12-05
# E105,Vikram Singh,Operations,58000,2022-01-11
# E109,Arumukesh,IT,38000,2025-10-10
# Enter choice3
# Enter Employee ID to search: E109
# Employee Found: ID: E109, Name: Arumukesh, Department: IT, Salary: 38000, Joining Date: 2025-10-10
# Enter choice4
# Enter Employee ID to update salary: E109
# Enter new Salary: 400000 
# Salary updated for Employee ID: E109
# Enter choice5
# Department:HR |No. Of employees:2| Total Salary:122000.0| average salary:61000.0
# Department:IT |No. Of employees:2| Total Salary:475000.0| average salary:237500.0
# Department:Finance |No. Of employees:1| Total Salary:55000.0| average salary:55000.0
# Department:Operations |No. Of employees:1| Total Salary:58000.0| average salary:58000.0
# Enter choice6
# enter EMP_IDE103
# Enter your choice:

# 6
# enter EMP_ID: E103
# Item deleted
# Enter choice7
