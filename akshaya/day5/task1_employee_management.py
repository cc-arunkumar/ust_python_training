#employee management using file handling
from datetime import date
import os


def initialize_file():

    if not os.path.exists("employees.txt") or os.path.getsize("employees.txt") == 0:
        with open("employees.txt", "w") as file:
            file.write("E101,Neha Sharma,HR,60000,2020-05-10\n")
            file.write("E102,Ravi Kumar,IT,75000,2019-08-21\n")
            file.write("E103,Arjun Mehta,Finance,55000,2021-03-15\n")
            file.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
            file.write("E105,Vikram Singh,Operations,58000,2022-01-11\n")
        print("Sample data initialized.\n")
    else:
        print("Existing file found. Using current data.\n")


def add_employee():
    emp_id = input("Enter Employee ID: ").strip()
    name = input("Enter Name: ").strip()
    dept = input("Enter Department: ").strip()
    salary = input("Enter Salary: ").strip()
    join_date = input("Enter Joining Date (YYYY-MM-DD): ").strip()

  
    if not salary.isdigit():
        print("Salary must be a numeric value!")
        return

  
    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                print("Employee ID already exists!")
                return

    
    with open("employees.txt", "a") as file:
        file.write(f"{emp_id},{name},{dept},{salary},{join_date}\n")

    print("Employee added successfully!")


def display_all():
    with open("employees.txt", "r") as file:
        lines = file.readlines()

    if not lines:
        print("No employee records found.")
        return

    print("\nEmployee Records:")
    print("-" * 70)
    print(f"{'ID':<8}{'Name':<20}{'Department':<15}{'Salary':<12}{'Join Date'}")
    print("-" * 70)

    for line in lines:
        emp_id, name, dept, salary, join_date = line.strip().split(",")
        print(f"{emp_id:<8}{name:<20}{dept:<15}{salary:<12}{join_date}")
    print("-" * 70)



def search_employee():
    emp_id = input("Enter Employee ID to search: ").strip()
    found = False

    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                emp_id, name, dept, salary, join_date = line.strip().split(",")
                print("\nEmployee Found:")
                print("-" * 60)
                print(f"ID: {emp_id}")
                print(f"Name: {name}")
                print(f"Department: {dept}")
                print(f"Salary: {salary}")
                print(f"Joining Date: {join_date}")
                print("-" * 60)
                found = True
                break

    if not found:
        print("Employee not found.")


def update_salary():
    emp_id = input("Enter Employee ID: ").strip()
    new_salary = input("Enter New Salary: ").strip()

    if not new_salary.isdigit():
        print("Salary must be a numeric value!")
        return

    updated = False

    with open("employees.txt", "r") as file:
        lines = file.readlines()

    with open("employees.txt", "w") as file:
        for line in lines:
            if line.startswith(emp_id + ","):
                parts = line.strip().split(",")
                parts[3] = new_salary
                file.write(",".join(parts) + "\n")
                updated = True
            else:
                file.write(line)

    if updated:
        print("Salary updated successfully!")
    else:
        print("Employee not found.")


def generate_report():
    dept_summary = {}

    with open("employees.txt", "r") as f:
        for line in f:
            if not line.strip():
                continue
            emp_id, name, dept, salary, join_date = line.strip().split(",")
            salary = float(salary)

            if dept not in dept_summary:
                dept_summary[dept] = {"count": 0, "total": 0}

            dept_summary[dept]["count"] += 1
            dept_summary[dept]["total"] += salary

    if not dept_summary:
        print("No data to generate report.")
        return

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("=== Department Salary Report ===\n")
        f.write(f"Generated on: {date.today()}\n\n")
        for dept, data in dept_summary.items():
            avg_salary = data["total"] / data["count"]
            f.write(f"{dept} Department → Employees: {data['count']} | "
                    f"Total Salary: {data['total']:.2f} | "
                    f"Average Salary: {avg_salary:.2f}\n")

    print("Report generated successfully! (Saved as report.txt)")



def delete_employee():
    emp_id = input("Enter Employee ID to delete: ").strip()
    deleted = False

    with open("employees.txt", "r") as f:
        lines = f.readlines()

    with open("employees.txt", "w") as f:
        for line in lines:
            if line.startswith(emp_id + ","):
                deleted = True
                continue
            f.write(line)

    if deleted:
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")



def main():
    initialize_file()

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
            add_employee()
        elif choice == "2":
            display_all()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_salary()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            delete_employee()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

#sample output
# Existing file found. Using current data.


# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 1
# Enter Employee ID:  E106
# Enter Name:  Meera Nair
# Enter Department:  HR
# Enter Salary:  64000
# Enter Joining Date (YYYY-MM-DD):  2022-11-20
# Employee added successfully!

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
# ----------------------------------------------------------------------
# ID      Name                Department     Salary      Join Date
# ----------------------------------------------------------------------
# E101    Neha Sharma         HR             60000       2020-05-10
# E102    Ravi Kumar          IT             75000       2019-08-21
# E103    Arjun Mehta         Finance        55000       2021-03-15
# E104    Fatima Khan         HR             62000       2018-12-05
# E105    Vikram Singh        Operations     58000       2022-01-11
# E106    Meera Nair          HR             64000       2022-11-20
# ----------------------------------------------------------------------

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 3
# Enter Employee ID to search:  E103

# Employee Found:
# ------------------------------------------------------------
# ID: E103
# Name: Arjun Mehta
# Department: Finance
# Salary: 55000
# Joining Date: 2021-03-15
# ------------------------------------------------------------

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 4
# Enter Employee ID:  E104
# Enter New Salary:  65000
# Salary updated successfully!

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 5
# Report generated successfully! (Saved as report.txt)

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 6
# Enter Employee ID to delete: E105
# Employee deleted successfully!

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 7
# Exiting program. Goodbye!
