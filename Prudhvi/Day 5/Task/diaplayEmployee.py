import employeemanagement

def display_employees():
    with open(employeemanagement.EMPLOYEE_FILE) as file:
        lines = file.readlines()
    # if not lines: print("No records."); return
    for line in lines:
        print(" | ".join(line.strip().split(",")))