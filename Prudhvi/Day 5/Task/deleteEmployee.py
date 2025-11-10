import employeemanagement

def delete_employee():
    eid = input("Enter ID to delete: ")
    lines = open(employeemanagement.EMPLOYEE_FILE).readlines() 
    deleted = False
    with open(employeemanagement.EMPLOYEE_FILE, "w") as file:
        for line in lines:
            if not line.startswith(eid + ","): 
                file.write(line)
            else: 
                deleted = True
    print("Deleted!" if deleted else "Not found.")

