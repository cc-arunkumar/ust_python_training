def add_emp():
    emp_unique=set()

    with open("employees.txt","r") as file:
        for line in file:
            details=line.strip().split(",")
            emp_unique.add(details[0])
    emp_id=input("Enter Employee ID: ")
    name=input("Enter Employee Name: ")
    dept=input("Enter Department: ")    
    salary=input("Enter Salary: ")
    joining_date=input("Enter Joining Date (YYYY-MM-DD): ")
    if emp_id not in emp_unique:
        with open("employees.txt","a") as file:
            file.write(f"\n{emp_id},{name},{dept},{salary},{joining_date}")
        with open("employees.txt","r") as file:
            content=file.read()
            print("employee details:\n",content)