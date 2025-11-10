import employeemanagement

def generate_report():
    department_summary = {}
    for emp_id, name, dept, salary in employeemanagement.EMPLOYEE_FILE:
        if dept not in department_summary:
            department_summary[dept] = {'total_salary': 0, 'employee_count': 0}

        department_summary[dept]['total_salary'] += salary
        department_summary[dept]['employee_count'] += 1

    with open("report.txt", "w", encoding= "utf-8") as file:
        for dept, data in department_summary.items():
            avg_salary = data['total_salary'] / data['employee_count']
            file.write(f"{dept} Department  Employees: {data['employee_count']} | Total Salary: {data['total_salary']} | Average Salary: {avg_salary}\n")

    print("Department-wise summary report has been written to report.txt.")
    