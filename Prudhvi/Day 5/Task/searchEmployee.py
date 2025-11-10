import employeemanagement

def search_employee():
    eid = input("Enter ID: "); found = False
    with open(employeemanagement.EMPLOYEE_FILE) as f:
        for line in f:
            if line.startswith(eid + ","):
                print("Found:", " | ".join(line.strip().split(",")))
                found = True
    if not found: print("Not found.")

