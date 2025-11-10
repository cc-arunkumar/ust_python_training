from write import add_new_employee
from read import read
from search import search
from update import update
from generate_dept import generate_department_report
from delete import delete
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

        if choice == "1":
            add_new_employee()
        elif choice == "2":
            read()
        elif choice == "3":
            search()
        elif choice == "4":
            update()
        elif choice == "5":
            generate_department_report()
        elif choice == "6":
            delete()
        elif choice == "7":
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

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
# Enter your choice: 1
# Enter Employee ID: E106
# Enter Full Name: Harsh Jaiswal
# Enter Department: IT
# Enter Salary: 70000
# Enter Date of Joining (YYYY-MM-DD): 2025-11-03
#  Employee added successfully.

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 2
# E101,Neha Sharma,HR,60000,2020-05-10
# E102,Ravi Kumar,IT,75000,2019-08-21
# E103,Arjun Mehta,Finance,55000,2021-03-15
# E104,Fatima Khan,HR,62000,2018-12-05
# E105,Vikram Singh,Operations,58000,2022-01-11
# E106,Harsh Jaiswal,IT,70000,2025-11-03


# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 3
# Enter the id:E106

#  Employee Found:
# ID: E106
# Name: Harsh Jaiswal
# Department: IT
# Salary: 70000
# Date of Joining: 2025-11-03

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 4
# Enter Employee ID to update salary: E106
# Enter New Salary: 100000
# ID: E106
# Name: Harsh Jaiswal
# Department: IT
# Salary: 100000
# Date of Joining: 2025-11-03

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 5
#  Report saved to 'report.txt'.

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 6
# Enter Employee ID to delete: E106
# Employee ID E106 deleted successfully.

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 7
#  Exiting program. Goodbye!