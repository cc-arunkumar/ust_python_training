import employeemanagement

def update_salary():
    eid = input("Enter ID: "); new_salary = input("New Salary: ")
    lines = open(employeemanagement.EMPLOYEE_FILE).readlines(); updated = False
    with open(employeemanagement.EMPLOYEE_FILE, "w") as file:
        for line in lines:
            parts = line.strip().split(",")
            if parts[0] == eid:
                parts[3] = new_salary; updated = True
            file.write(",".join(parts) + "\n")
    print("Updated!" if updated else "Not found.")
