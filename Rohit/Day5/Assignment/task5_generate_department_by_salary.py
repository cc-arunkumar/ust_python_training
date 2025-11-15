# Generate Department-wise Summary Report
# Read all employee records.
# Count how many employees work in each department.
# Calculate total and average salary per department.
# Write the summary to a new file called report.txt .
import os

employees = {}

if os.path.exists("employee.txt"):
    with open("employee.txt", "r", encoding="utf-8") as file:
        for line in file:
            tokens = line.strip().split(",")
            if len(tokens) == 5:
                emp_id, name, dept, salary, join_date = tokens
                try:
                    salary = float(salary)
                except ValueError:
                    continue  
                employees[emp_id] = {
                    "name": name,
                    "department": dept,
                    "salary": salary,
                    "join_date": join_date
                }
else:
    print("employee.txt not found.")
    exit()

print(employees)

department_summary = {}

for data in employees.values():
    dept = data["department"]
    salary = data["salary"]
    if dept not in department_summary:
        department_summary[dept] = {"count": 0, "total_salary": 0.0}
    department_summary[dept]["count"] += 1
    department_summary[dept]["total_salary"] += salary
print(department_summary)

with open("report.txt", "w", encoding="utf-8") as report:
    for dept, stats in department_summary.items():
        print(dept)
        print(stats)
        avg_salary = stats["total_salary"] / stats["count"]
        total_salary = stats["total_salary"]
        report.write(
            f"{dept} Department → Employees: {stats['count']} | "
            f"Total Salary: {total_salary:.1f} | "
            f"Average Salary: {avg_salary:.1f}\n"
        )

print("Department-wise summary written to report.txt.")
# ==============sample output====================
# Department-wise summary written to report.txt.
# HR Department → Employees: 2 | Total Salary: 122000.0 | Average Salary: 61000.0
# IT Department → Employees: 1 | Total Salary: 75000.0 | Average Salary: 75000.0
# Finance Department → Employees: 1 | Total Salary: 55000.0 | Average Salary: 55000.0
# Operations Department → Employees: 1 | Total Salary: 58000.0 | Average Salary: 58000.0
