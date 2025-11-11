#Task1: HR Employee Record Management System

#Create a employee file to store data
with open("employee.txt","w") as file:
    file.write("E101,Neha Sharma,HR,60000,2020-05-10\n")
    file.write("E102,Ravi Kumar,IT,75000,2019-08-21\n")
    file.write("E103,Arjun Mehta,Finance,55000,2021-03-15\n")
    file.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
    file.write("E105,Vikram Singh,Operations,58000,2022-01-11\n")

#Add employee to the data
def add_employee():
    with open("employee.txt","a") as file:
        emp_id = input("Enter Employee ID: ")
        emp_name = input("Enter Name: ")
        emp_dept = input("Enter dept: ")
        emp_sal = input("Enter Salary: ")
        emp_join_dt = input("Enter Joining Date (YYYY-MM-DD): ")
        file.write(f"{emp_id},{emp_name},{emp_dept},{emp_sal},{emp_join_dt}")

#Search employee in the data with Employee ID
def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    with open("employee.txt","r") as file:
        for line in file:
            if emp_id in line:
                data = line.strip().split(",")
                format_data = "|".join(data)
                print(format_data)

#Display all employee details from the data
def display_employee():
    with open("employee.txt","r") as file:
        for line in file:
            data = line.strip().split(",")
            format_data = "|".join(data)
            print(format_data)

#Update salary of employee
def update_salary():
    e_id = input("Enter Employee ID:")
    updated_sal = input("Enter New Salary:")
    with open("employee.txt","r") as file:
        lines = file.readlines()
        is_found = False
        i=0
        for line in lines:
            li = line.strip().split(",")
            if li[0]==e_id:
                is_found =True
                li[3]=updated_sal
                print(",".join(li))
                lines[i] = ",".join(li)
                lines[i] = lines[i]+"\n"
            i += 1
        if not is_found:
            print("Employee not found")
    with open("employee.txt","w") as file:
        file.writelines(lines)

#Department report                    
def dept_report():
    from collections import defaultdict
    dept_data=defaultdict(lambda:{"count":0,"total_salary":0})
    with open("employee.txt",'r') as file:
        for line in file:
            content=line.strip().split(",")
            if len(content)>=4:
                dept=content[2]
                sal=float(content[3])
                dept_data[dept]['count']+=1
                dept_data[dept]['total_salary']+=sal
                    
    with open("Report.txt",'w') as file:
        for dept,data in dept_data.items():
            count=data['count']
            total_salary=data["total_salary"]
            avg_sal=total_salary/count if count else 0
            file.write(f"{dept} Department-->Employees: {count} | Total Salary: {float(total_salary)} | Average Salary: {avg_sal}\n")

#Delete employee data        
def delete_employee_data():
    emp_id = input("Enter the emp_id of the employee to delete: ")
    with open("employee.txt",'r') as file:
        lines = file.readlines()
    
    found = False
    
    with open("employee.txt",'w') as file:
        for line in lines:
            if line.startswith(emp_id):
                found = True
            else:
                file.write(line)
    
    if found:
        print(f"Employee with emp_id {emp_id} has been deleted.")
    else:
        print(f"No employee found with emp_id {emp_id}.")



print("==== Employee Record Management ====")
print("1. Add New Employee")
print("2. Display All Employees")
print("3. Search Employee by ID")
print("4. Update Employee Salary")
print("5. Generate Department Report")
print("6. Delete Employee")
print("7. Exit")

while True:
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            add_employee()
        case 2:
            display_employee()
        case 3:
            search_employee()
        case 4:
            update_salary()
        case 5:
            dept_report()
        case 6:
            delete_employee_data()
        case 7:
            break
       
        
#Sample Execution
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
# Enter Name: Meera Nair
# Enter dept: HR
# Enter Salary: 64000
# Enter Joining Date (YYYY-MM-DD): 2022-11-20
# Enter your choice: 2
# E101|Neha Sharma|HR|60000|2020-05-10
# E102|Ravi Kumar|IT|75000|2019-08-21
# E103|Arjun Mehta|Finance|55000|2021-03-15
# E104|Fatima Khan|HR|62000|2018-12-05
# E105|Vikram Singh|Operations|58000|2022-01-11
# E106|Meera Nair|HR|64000|2022-11-20
# Enter your choice: 3
# Enter Employee ID to search: E102
# E102|Ravi Kumar|IT|75000|2019-08-21
# Enter your choice: 4
# Enter Employee ID:E103
# Enter New Salary:60000
# E103,Arjun Mehta,Finance,60000,2021-03-15
# Enter your choice: 5
# HR Department-->Employees: 3 | Total Salary: 186000.0 | Average Salary: 62000.0
# IT Department-->Employees: 1 | Total Salary: 75000.0 | Average Salary: 75000.0
# Finance Department-->Employees: 1 | Total Salary: 55000.0 | Average Salary: 55000.0
# Operations Department-->Employees: 1 | Total Salary: 58000.0 | Average Salary: 58000.0
# Enter your choice: 6
# Enter the emp_id of the employee to delete: E102
# Employee with emp_id E102 has been deleted.