with open("employees.txt",'w') as file:
        file.write("E101,Neha Sharma,HR,60000,2020-05-10\n")
        file.write("E102,Ravi Kumar,IT,75000,2019-08-21\n")
        file.write("E103,Arjun Mehta,Finance,55000,2021-03-15\n")
        file.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
        file.write("E105,Vikram Singh,Operations,58000,2022-01-11\n")
while(True):
    print("==== Employee Record Management ====")
    print("1. Add New Employee\n")
    print("2. Display All Employees\n")
    print("3. Search Employee by ID\n")
    print("4. Update Employee Salary\n")
    print("5. Generate Department Report\n")
    print("6. Delete Employee\n")
    print("7. Exit\n")
    chc=input("Enter your choice: ")

    
    if chc=='1':
        id=input("Enter Employee ID: ")
        name=input("Enter Name: ")
        dept=input("Enter Department: ")
        sal=input("Enter Salary: ")
        date=input("Enter Joining Date (YYYY-MM-DD): ")

        with open("employees.txt",'a') as file:
            file.write(f"{id},")
            file.write(f"{name},")
            file.write(f"{dept},")
            file.write(f"{sal},")
            file.write(f"{date}")
        print("Employee added successfully\n")
    elif chc=='2':
        def read_records():
            with open("employees.txt", "r") as file:
                records = []
                for line in file:
                    line = line.strip()         
                    if line:                     
                        a= line.split(",")  
                        records.append(a)
                return records

        print("Employee Records\n")
        rec=read_records()
        for r in rec:
            print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]}")
    elif chc=='3':
        def search_emp(seach):
            with open("employees.txt","r") as file:
                for line in file:
                    if search in line:
                        return "Employee Found"
                return "Employee not Found"
        search=input("Enter Employee ID to search: ")
        print(search_emp(search))

    elif chc=='4':
        def read_records():
            with open("employees.txt", "r") as file:
                records = []
                for line in file:
                    line = line.strip()         
                    if line:                     
                        a= line.split(",")  
                        records.append(a)
                return records
        emp_id = input("Enter Employee ID: ")
        new_salary = input("Enter New Salary: ")
        updated_line=[]
        up=read_records()
        for a in up:
            if a[0]==emp_id:
                a[3]=new_salary
            updated_line.append(",".join(a) + "\n")

        with open("employees.txt", "w") as file:
            for line in updated_line:
                file.write(line)
        print("Salary updated succefully\n")

    elif chc=='5':
        rec = read_records()
        dep = {}
        for r in rec:
            dept = r[2]
            sal = float(r[3])
            if dept not in dep:
                dep[dept] = {"count": 0, "total_salary": 0.0}

            dep[dept]["count"] += 1
            dep[dept]["total_salary"] += sal

        with open("report.txt", "w", encoding="utf-8") as f1:
            for dept, val in dep.items():
                count = val["count"]
                tot_sal = val["total_salary"]
                avg_sal = tot_sal / count
                f1.write(
                    f"{dept}Department→Employees:{count}|Total Salary:{tot_sal}|Average Salary:{avg_sal}\n"
                )
        print("Employee stores in report file\n")

    elif chc=='6':
        dele=input("Enter Employee ID to delete: ")
        up=read_records()
        updated_record=[]
        for b in up:
            if b[0]!=dele:
                updated_record.append(b)
        with open("employees.txt",'w') as f2:
            for i in updated_record:
                f2.write(",".join(i)+"\n")
        print("Employee deleted successfully")
    elif chc=='7':
        print("Exiting...")
        break
    else:
        print("Invalid choice")



##Sample Output

# ==== Employee Record Management ====
# 1. Add New Employee

# 2. Display All Employees

# 3. Search Employee by ID

# 4. Update Employee Salary

# 5. Generate Department Report

# 6. Delete Employee

# 7. Exit

# Enter your choice: 1
# Enter Employee ID: E106
# Enter Name: Deva
# Enter Department: IT
# Enter Salary: 100000
# Enter Joining Date (YYYY-MM-DD): 2025-03-10
# Employee added successfully

# ==== Employee Record Management ====
# 1. Add New Employee

# 2. Display All Employees

# 3. Search Employee by ID

# 4. Update Employee Salary

# 5. Generate Department Report

# 6. Delete Employee

# 7. Exit

# Enter your choice: 2
# Employee Records

# E101 | Neha Sharma | HR | 60000 | 2020-05-10
# E102 | Ravi Kumar | IT | 75000 | 2019-08-21
# E103 | Arjun Mehta | Finance | 55000 | 2021-03-15
# E104 | Fatima Khan | HR | 62000 | 2018-12-05
# E105 | Vikram Singh | Operations | 58000 | 2022-01-11
# E106 | Deva | IT | 100000 | 2025-03-10
# ==== Employee Record Management ====
# 1. Add New Employee

# 2. Display All Employees

# 3. Search Employee by ID

# 4. Update Employee Salary

# 5. Generate Department Report

# 6. Delete Employee

# 7. Exit

# Enter your choice: 3
# Enter Employee ID to search: E106
# Employee Found
# ==== Employee Record Management ====
# 1. Add New Employee

# 2. Display All Employees

# 3. Search Employee by ID

# 4. Update Employee Salary

# 5. Generate Department Report

# 6. Delete Employee

# 7. Exit

# Enter your choice: 4
# Enter Employee ID: E106
# Enter New Salary: 234556
# Salary updated succefully

# ==== Employee Record Management ====
# 1. Add New Employee

# 2. Display All Employees

# 3. Search Employee by ID

# 4. Update Employee Salary

# 5. Generate Department Report

# 6. Delete Employee

# 7. Exit

# Enter your choice: 5
# Employee stores in report file

# ==== Employee Record Management ====
# 1. Add New Employee

# 2. Display All Employees

# 3. Search Employee by ID

# 4. Update Employee Salary

# 5. Generate Department Report

# 6. Delete Employee

# 7. Exit

# Enter your choice: 6
# Enter Employee ID to delete: E106
# Employee deleted successfully
# ==== Employee Record Management ====
# 1. Add New Employee

# 2. Display All Employees

# 3. Search Employee by ID

# 4. Update Employee Salary

# 5. Generate Department Report

# 6. Delete Employee

# 7. Exit

# Enter your choice: 7
# Exiting...