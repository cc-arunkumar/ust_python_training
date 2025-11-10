def search_emp():
    emp_id=input ("Enter Employee ID to search: ")
    found=False
    with open("employees.txt","r") as file:
        for line in file:
            details=line.strip().split(",")
            if details[0]==emp_id:
                print(f"Employee Found: ID: {details[0]}, Name: {details[1]}, Department: {details[2]}, Salary: {details[3]}, Joining Date: {details[4]}")
                found=True
                break

# search_emp()