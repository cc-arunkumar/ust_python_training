import employeemanagement

def generate_report():
    summary = {}
    with open(employeemanagement.EMPLOYEE_FILE) as f:
        for line in f:
            eid, name, dept, salary, date = line.strip().split(",")
            salary = float(salary)
            if dept not in summary:
                summary[dept] = {"count": 0, "total": 0}
            summary[dept]["count"] += 1
            summary[dept]["total"] += salary

    with open(employeemanagement.REPORT_FILE, "w") as r:
        for dept, data in summary.items():
            avg = data["total"] / data["count"]
            r.write(
                f"{dept}: Employees={data['count']} | "
                f"Total={data['total']} | Avg={avg:.2f}\n"
            )

    print("Report generated!")
