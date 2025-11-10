def generate_department_report():
    departments = []
    counts = []
    totals = []

    with open("employees.txt", "r") as file:
        for line in file:
            fields = line.strip().split(",")
            dept = fields[2].strip()
            salary = float(fields[3].strip())

            if dept in departments:
                i = departments.index(dept)
                counts[i] += 1
                totals[i] += salary
            else:
                departments.append(dept)
                counts.append(1)
                totals.append(salary)

   
    with open("report.txt", "w") as report:
        report.write("Department Report\n")
        report.write("=================\n")
        for i in range(len(departments)):
            avg = totals[i] / counts[i]
            report.write(f"Department: {departments[i]}\n")
            report.write(f"  Employees: {counts[i]}\n")
            report.write(f"  Total Salary: {totals[i]:.2f}\n")
            report.write(f"  Average Salary: {avg:.2f}\n")

    print(" Report saved to 'report.txt'.")
