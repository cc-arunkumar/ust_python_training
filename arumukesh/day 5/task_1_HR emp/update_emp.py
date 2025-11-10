def update_sal():

    emp_id=input("Enter Employee ID to update salary: ")
    new_salary=input("Enter new Salary: ")
    emp=[]
    with open("employees.txt","r") as file:
        for line in file:
            details=line.strip().split(",")
            if details[0]==emp_id:
                details[3]=new_salary
                print(f"Salary updated for Employee ID: {emp_id}")
            
            emp.append(",".join(details)+"\n")
    with open("employees.txt","w") as files:
        for det in emp:
            files.write(det)