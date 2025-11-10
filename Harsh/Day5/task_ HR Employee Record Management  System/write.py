with open("employees.txt","w")as file:
    file.write("E101,Neha Sharma,HR,60000,2020-05-10\n")
    file.write("E102,Ravi Kumar,IT,75000,2019-08-21\n")
    file.write("E103,Arjun Mehta,Finance,55000,2021-03-15\n")
    file.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
    file.write("E105,Vikram Singh,Operations,58000,2022-01-11\n")
    
def add_new_employee():
    emp_id = input("Enter Employee ID: ").strip()
    name = input("Enter Full Name: ").strip()
    department = input("Enter Department: ").strip()
    salary = input("Enter Salary: ").strip()
    doj = input("Enter Date of Joining (YYYY-MM-DD): ").strip()

    with open("employees.txt", "r") as file:
        for line in file:
            existing_id = line.strip().split(",")[0]
            if emp_id == existing_id:
                print("Employee ID already exists.")
                return

    with open("employees.txt", "a") as file:
        file.write(f"{emp_id},{name},{department},{salary},{doj}\n")
    print(" Employee added successfully.")

