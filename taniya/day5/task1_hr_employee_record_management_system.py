import os

# Step 1: Create and write initial employee records into employee.txt
with open("employee.txt", "w") as file:
    file.write("E101,Neha Sharma,HR,60000,2020-05-10\n")
    file.write("E102,Ravi Kumar,IT,75000,2019-08-21\n")
    file.write("E103,Arjun Mehta,Finance,55000,2021-03-15\n")
    file.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
    file.write("E105,Vikram Singh,Operations,58000,2022-01-11\n")

# Step 2: Add new employee (check duplicate ID before adding)
print("\nAdd New Employee")
new_id = input("Enter Employee ID: ")
with open("employee.txt", "r") as file:
    # Check if employee ID already exists
    if any(line.startswith(new_id) for line in file):
        print("Employee ID already exists. Cannot add duplicate.")
    else:
        # Collect new employee details
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = input("Enter Salary: ")
        doj = input("Enter Joining Date (YYYY-MM-DD): ")
        # Append new employee record
        with open("employee.txt", "a") as file:
            file.write(f"{new_id},{name},{dept},{salary},{doj}\n")
        print("Employee added successfully.")

# Step 3: Display all employees
print("\nDisplay All Employees")
if os.path.exists("employee.txt"):
    with open("employee.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            print("No employee records found.")
        else:
            print("Employee Records:")
            # Print each employee record in formatted way
            for line in lines:
                print(" , ".join(line.strip().split(',')))
else:
    print("File not found.")

# Step 4: Search employee by ID
print("\nSearch Employee by ID")
emp_id = input("Enter Employee ID to search: ")
found = False
with open("employee.txt", "r") as file:
    for line in file:
        if line.startswith(emp_id):
            print("Employee Found:")
            print(" , ".join(line.strip().split(',')))
            found = True
            break
if not found:
    print("Employee not found.")

# Step 5: Update employee salary
print("\nUpdate Employee Salary")
emp_id = input("Enter Employee ID to update salary: ")
new_salary = input("Enter new salary: ")
found = False
# Read all lines first
with open("employee.txt", "r") as file:
    lines = file.readlines()
# Rewrite file with updated salary if match found
with open("employee.txt", "w") as file:
    for line in lines:
        if line.startswith(emp_id):
            parts = line.strip().split(',')
            parts[3] = new_salary  # Update salary field
            updated_line = ",".join(parts)
            file.write(updated_line + "\n")
            found = True
            print("Salary updated successfully:")
            print(" , ".join(parts))
        else:
            file.write(line)
if not found:
    print("Employee not found.")

# Step 6: Delete employee record
print("\nDelete Employee Record")
emp_id = input("Enter Employee ID to delete: ")
found = False
with open("employee.txt", "r") as file:
    lines = file.readlines()
with open("employee.txt", "w") as file:
    for line in lines:
        if line.startswith(emp_id):
            found = True  # Skip writing this line (deletes employee)
        else:
            file.write(line)
if found:
    print(f"Employee {emp_id} deleted successfully!")
else:
    print("Employee not found.")

# Step 7: Generate department-wise summary report
print("Department-wise Summary Report...")
dept_summary = {}
with open("employee.txt", "r") as file:
    for line in file:
        parts = line.strip().split(',')
        dept = parts[2]
        salary = int(parts[3])
        # Initialize department summary if not present
        if dept not in dept_summary:
            dept_summary[dept] = {'count': 0, 'total_salary': 0}
        # Update count and salary totals
        dept_summary[dept]['count'] += 1
        dept_summary[dept]['total_salary'] += salary

# Save summary report to report.txt
with open("report.txt", "w", encoding="utf-8") as report:
    for dept, data in dept_summary.items():
        avg_salary = data['total_salary'] / data['count']
        report.write(f"{dept} Department → Employees: {data['count']} | "
                     f"Total Salary: {data['total_salary']} | "
                     f"Average Salary: {avg_salary:.1f}\n")

print("Report saved to report.txt")


# output
# Add New Employee
# Enter Employee ID: E106
# Enter Name: Taniya
# Enter Department: SDE
# Enter Salary: 50000
# Enter Joining Date (YYYY-MM-DD): 2025-11-03
# Employee added successfully.

# Display All Employees       
# Employee Records:
# E101 , Neha Sharma , HR , 60000 , 2020-05-10
# E102 , Ravi Kumar , IT , 75000 , 2019-08-21
# E103 , Arjun Mehta , Finance , 55000 , 2021-03-15
# E104 , Fatima Khan , HR , 62000 , 2018-12-05
# E105 , Vikram Singh , Operations , 58000 , 2022-01-11
# E106 , Taniya , SDE , 50000 , 2025-11-03

# Search Employee by ID
# Enter Employee ID to search: E102
# Employee Found:
# E102 , Ravi Kumar , IT , 75000 , 2019-08-21

# Update Employee Salary
# Enter Employee ID to update salary: E101
# Enter new salary: 70000
# Salary updated successfully:
# E101 , Neha Sharma , HR , 70000 , 2020-05-10

# Delete Employee Record
# Enter Employee ID to delete: E106
# Employee E106 deleted successfully!
# Department-wise Summary Report...
# Report saved to report.txt