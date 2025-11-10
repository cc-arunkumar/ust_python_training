import os
from datetime import datetime

EMPLOYEE_FILE = 'employees.txt'
REPORT_FILE = 'report.txt'

def add_employee():
    emp_id = input("Enter Employee ID: ").strip()
    if not emp_id:
        print("Employee ID cannot be empty.")
        return

    if os.path.exists(EMPLOYEE_FILE):
        with open(EMPLOYEE_FILE, 'r') as f:
            for line in f:
                if line.startswith(emp_id + ','):
                    print("Employee ID already exists.")
                    return

    name = input("Enter Name: ").strip()
    dept = input("Enter Department: ").strip()
    try:
        salary = float(input("Enter Salary: ").strip())
    except ValueError:
        print("Invalid salary. Must be a number.")
        return
    join_date = input("Enter Joining Date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(join_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format.")
        return

    with open(EMPLOYEE_FILE, 'a') as f:
        f.write(f"{emp_id},{name},{dept},{salary},{join_date}\n")
    print("Employee added successfully!")

def display_employees():
    if not os.path.exists(EMPLOYEE_FILE) or os.path.getsize(EMPLOYEE_FILE) == 0:
        print("No employee records found.")
        return

    print("Employee Records:")
    with open(EMPLOYEE_FILE, 'r') as f:
        for line in f:
            emp_id, name, dept, salary, join_date = line.strip().split(',')
            print(f"{emp_id} | {name} | {dept} | {salary} | {join_date}")

def search_employee():
    emp_id = input("Enter Employee ID to search: ").strip()
    found = False
    with open(EMPLOYEE_FILE, 'r') as f:
        for line in f:
            if line.startswith(emp_id + ','):
                emp_id, name, dept, salary, join_date = line.strip().split(',')
                print("Employee Found:")
                print(f"{emp_id} | {name} | {dept} | {salary} | {join_date}")
                found = True
                break
    if not found:
        print("Employee not found.")

def update_salary():
    emp_id = input("Enter Employee ID: ").strip()
    try:
        new_salary = float(input("Enter New Salary: ").strip())
    except ValueError:
        print("Invalid salary.")
        return

    updated = False
    lines = []
    with open(EMPLOYEE_FILE, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if parts[0] == emp_id:
                parts[3] = str(new_salary)
                updated = True
            lines.append(','.join(parts))

    if updated:
        with open(EMPLOYEE_FILE, 'w') as f:
            for line in lines:
                f.write(line + '\n')
        print("Salary updated successfully!")
    else:
        print("Employee not found.")

def generate_report():
    summary = {}
    if not os.path.exists(EMPLOYEE_FILE):
        print("No employee records found.")
        return

    with open(EMPLOYEE_FILE, 'r') as f:
        for line in f:
            _, _, dept, salary, _ = line.strip().split(',')
            salary = float(salary)
            if dept not in summary:
                summary[dept] = {'count': 0, 'total': 0}
            summary[dept]['count'] += 1
            summary[dept]['total'] += salary

    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        for dept, data in summary.items():
            avg = data['total'] / data['count']
            f.write(f"{dept} Department -> Employees: {data['count']} | Total Salary: {data['total']} | Average Salary: {avg:.1f}\n")

    print("Report generated successfully!")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ").strip()
    deleted = False
    lines = []
    with open(EMPLOYEE_FILE, 'r') as f:
        for line in f:
            if not line.startswith(emp_id + ','):
                lines.append(line.strip())
            else:
                deleted = True

    if deleted:
        with open(EMPLOYEE_FILE, 'w') as f:
            for line in lines:
                f.write(line + '\n')
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")

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

        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_salary()
        elif choice == '5':
            generate_report()
        elif choice == '6':
            delete_employee()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

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
# Enter your choice: 2
# No employee records found.

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 1
# Enter Employee ID: E101
# Enter Name: Bhargavi S
# Enter Department: IT
# Enter Salary: 50000
# Enter Joining Date (YYYY-MM-DD): 2021-11-02
# Employee added successfully!

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 1
# Enter Employee ID: E103
# Enter Name: Meena
# Enter Department: Fianace
# Enter Salary: 60000
# Enter Joining Date (YYYY-MM-DD): 2021-02-04
# Employee added successfully!

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 1
# Enter Employee ID: E103
# Employee ID already exists.

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: E104
# Invalid choice. Try again.

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 1
# Enter Employee ID: E103
# Employee ID already exists.

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 1
# Enter Employee ID: E104
# Enter Name: Swathi
# Enter Department: Health
# Enter Salary: 67000
# Enter Joining Date (YYYY-MM-DD): 2019-06-04
# Employee added successfully!

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 1
# Enter Employee ID: E105
# Enter Name: Yashu
# Enter Department: HR
# Enter Salary: 8000
# Enter Joining Date (YYYY-MM-DD): 2016-03-02
# Employee added successfully!

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
# Enter Name: Varsha
# Enter Department: HR
# Enter Salary: 45000
# Enter Joining Date (YYYY-MM-DD): 2015-03-02
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
# E101 | Bhargavi S | IT | 50000.0 | 2021-11-02
# E103 | Meena | Fianace | 60000.0 | 2021-02-04
# E104 | Swathi | Health | 67000.0 | 2019-06-04
# E105 | Yashu | HR | 8000.0 | 2016-03-02
# E106 | Varsha | HR | 45000.0 | 2015-03-02

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 3
# Enter Employee ID to search: E104
# Employee Found:
# E104 | Swathi | Health | 67000.0 | 2019-06-04

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 4
# Enter Employee ID: E101
# Enter New Salary: 45900
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
# Report generated successfully!

# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice: 6
# Enter Employee ID to delete: E104
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
# Exiting program.