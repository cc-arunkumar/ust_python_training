import employeemanagement


def add_employee():
    eid = input("ID: ") 
    name = input("Name: ")
    dept = input("Dept: ")
    salary = input("Salary: ")
    date = input("Joining Date (YYYY-MM-DD): ")
    with open(employeemanagement.EMPLOYEE_FILE, "a") as f:
        f.write(f"{eid},{name},{dept},{salary},{date}\n")
    print("Added!")

