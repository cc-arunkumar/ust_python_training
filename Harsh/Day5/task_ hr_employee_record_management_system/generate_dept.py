# Generate Department-wise Summary Report
# Read all employee records.
# Count how many employees work in each department.
# Calculate total and average salary per department.
# Write the summary to a new file called report.txt .
# Example output in report.txt :
# HR Department → Employees: 3 | Total Salary: 186000 | Average Salary: 6200
# 0.0
# IT Department → Employees: 1 | Total Salary: 75000 | Average Salary: 75000.0
# Finance Department → Employees: 1 | Total Salary: 55000 | Average Salary: 5
# 5000.0
# Operations Department → Employees: 1 | Total Salary: 58000 | Average Salar
# y: 58000.0

def generate_department_report():
    # Lists to store department names, employee counts, and total salaries
    departments = []
    counts = []
    totals = []

    # Open the employees.txt file in read mode
    with open("employees.txt", "r") as file:
        for line in file:
            # Split each line into fields: [ID, Name, Department, Salary, ...]
            fields = line.strip().split(",")
            dept = fields[2].strip()          # Extract department name
            salary = float(fields[3].strip()) # Extract salary as a number

            # If department already exists, update its count and total salary
            if dept in departments:
                i = departments.index(dept)   # Find index of department
                counts[i] += 1                # Increase employee count
                totals[i] += salary           # Add salary to total
            else:
                # If department is new, add it to the lists
                departments.append(dept)
                counts.append(1)
                totals.append(salary)

    # Write the department report to a new file
    with open("report.txt", "w") as report:
        report.write("Department Report\n")
        report.write("=================\n")
        for i in range(len(departments)):
            avg = totals[i] / counts[i]  # Calculate average salary
            report.write(f"Department: {departments[i]}\n")
            report.write(f"  Employees: {counts[i]}\n")
            report.write(f"  Total Salary: {totals[i]:.2f}\n")
            report.write(f"  Average Salary: {avg:.2f}\n")

    # Confirmation message
    print(" Report saved to 'report.txt'.")
