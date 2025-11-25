import os
import datetime
import addEmployee
import diaplayEmployee
import searchEmployee
import updateEmployee
import generateReport
import deleteEmployee


EMPLOYEE_FILE = "employees.txt"
REPORT_FILE = "report.txt"

if not os.path.exists(EMPLOYEE_FILE):
    with open(EMPLOYEE_FILE, "w") as file:
        file.write("E101,Neha Sharma,HR,60000,2020-05-10\n")
        file.write("E102,Ravi Kumar,IT,75000,2019-08-21\n")
        file.write("E103,Arjun Mehta,Finance,55000,2021-03-15\n")
        file.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
        file.write("E105,Vikram Singh,Operations,58000,2022-01-11\n")



while True:
    print("\n==== Employee Management ====")
    print("1.Add a new Employee")  
    print("2.Display all the employees")  
    print("3.Search an employee by EId") 
    print("4.Update the salary of an Employee")
    print("5.Generate the report of Employee")  
    print("6.Delete the details of an Employee")
    print("7.Exit")
    choice = input("Enter Your Choice: ")
    if choice=="1": addEmployee.add_employee()
    elif choice=="2": diaplayEmployee.display_employees()
    elif choice=="3": searchEmployee.search_employee()
    elif choice=="4": updateEmployee.update_salary()
    elif choice=="5": generateReport.generate_report()
    elif choice=="6": deleteEmployee.delete_employee()
    elif choice=="7": break
    else: print("Invalid!")
    
#Sample Output:
# ==== Employee Management ====
# ==== Employee Management ====
# 1.Add a new Employee
# 2.Display all the employees
# 3.Search an employee by EId
# 4.Update the salary of an Employee
# 5.Generate the report of Employee
# 6.Delete the details of an Employee
# 7.Exit
# Enter Your Choice: 2
# E101 | Neha Sharma | HR | 60000 | 2020-05-10
# E102 | Ravi Kumar | IT | 75000 | 2019-08-21
# E103 | Arjun Mehta | Finance | 55000 | 2021-03-15    
# E104 | Fatima Khan | HR | 62000 | 2018-12-05
# E105 | Vikram Singh | Operations | 58000 | 2022-01-11

# ==== Employee Management ====
# 1.Add a new Employee
# 2.Display all the employees
# 3.Search an employee by EId
# 4.Update the salary of an Employee
# 5.Generate the report of Employee
# 6.Delete the details of an Employee
# 7.Exit
# Enter Your Choice: 3
# Enter ID: E102
# Found: E102 | Ravi Kumar | IT | 75000 | 2019-08-21

# ==== Employee Management ====
# 1.Add a new Employee
# 2.Display all the employees
# 3.Search an employee by EId
# 4.Update the salary of an Employee
# 5.Generate the report of Employee
# 6.Delete the details of an Employee
# 7.Exit
# Enter Your Choice: 4
# Enter ID: E102
# New Salary: 59000
# Updated!

# ==== Employee Management ====
# 1.Add a new Employee
# 2.Display all the employees
# 3.Search an employee by EId
# 4.Update the salary of an Employee
# 5.Generate the report of Employee
# 6.Delete the details of an Employee
# 7.Exit
# Enter Your Choice: 5
# Report generated!

# ==== Employee Management ====
# 1.Add a new Employee
# 2.Display all the employees
# 3.Search an employee by EId
# 4.Update the salary of an Employee
# 5.Generate the report of Employee
# 6.Delete the details of an Employee
# 7.Exit
# Enter Your Choice: 6
# Enter ID to delete: E102
# Deleted!

# ==== Employee Management ====
# 1.Add a new Employee
# 2.Display all the employees
# 3.Search an employee by EId
# 4.Update the salary of an Employee
# 5.Generate the report of Employee
# 6.Delete the details of an Employee
# 7.Exit
# Enter Your Choice: 7


