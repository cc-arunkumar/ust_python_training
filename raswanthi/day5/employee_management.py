#Employee Management using File handling
import os

with open("employee.txt","w") as file:
    file.write("E101,Neha Sharma,HR,60000,2020-05-10\n")
    file.write("E102,Ravi Kumar,IT,75000,2019-08-21\n")
    file.write("E103,Nisha,Finance,55000,2021-03-15\n")
    file.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
    file.write("E105,Vikram Singh,Operations,58000,2022-01-11\n")

def add_employee():
    if os.path.exists("employee.txt"):
        with open("employee.txt","r") as file:
            content=file.read()
            print(content)
    else:
        print("The file does not exist\n ")
    emp_id=input("Enter Employee ID:")
    emp_name=input("Enter Name:")
    emp_dept=input("Enter Department:")
    emp_sal=float(input("Enter Salary:"))
    emp_joining=input("Enter the joining:")
    with open("employee.txt","a") as file:
        file.write(f"{emp_id},{emp_name},{emp_dept},{emp_sal},{emp_joining}\n")

def display_all_employees():
    with open("employee.txt","r") as file:
        print("Employee Records:")
        for each_line in file:
            print(" | ".join(each_line.strip().split(',')))

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    with open("employee.txt", 'r') as file:
        for each_line in file:
            if each_line.startswith(emp_id + ','):
                print("Employee Found:")
                print(" | ".join(each_line.strip().split(',')))
                found = True
                break
    if not found:
        print("Employee not found.")

def update_sal():
    emp_id=input("Enter Employee ID:")
    new_sal=input("Enter New Salary:")
    lines=[]
    with open("employee.txt","r") as file:
        for each_line in file:
            parts=each_line.strip().split(',')
            if parts[0]==emp_id:
                parts[3]=new_sal
            lines.append(",".join(parts))
    with open("employee.txt","w") as file:
        for each_line in lines:
            file.write(f"{each_line}\n")
    print("Salary is updated")

def generate_report():
    departments=[]
    dept_counts=[]
    dept_sal=[]

    with open("employee.txt","r") as file:
        for each_line in file:
            parts=each_line.strip().split(',')
            dept=parts[2]
            salary=float(parts[3])
            if dept in departments:
                index = departments.index(dept)
                dept_counts[index] += 1
                dept_sal[index] += salary
            else:
                departments.append(dept)
                dept_counts.append(1)
                dept_sal.append(salary)

    with open("report.txt", "w") as report:
        for i in range(len(departments)):
            avg_salary = dept_sal[i] / dept_counts[i]
            report.write(f"{departments[i]} Department -> Employees: {dept_counts[i]} | "
                         f"Total Salary: {dept_sal[i]} | "
                         f"Average Salary: {avg_salary:.1f}\n")
    print("Report Generated")

def delete_employee():
    emp_id=input("Enter Employee ID to delete:")
    deleted=False
    lines=[]
    with open("employee.txt","r") as file:
        for each_line in file:
            parts=each_line.strip().split(',')
            if not parts[0]==emp_id:
                lines.append(each_line)
            else:
                deleted=True
    with open("employee.txt", "w") as file:
        for each_line in lines:
            file.write(each_line)

    if deleted:
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")

print("----Employee Record Management----")
print("1.Add New Employee")
print("2.Display All Employees")
print("3.Search Employee by ID")
print("4.Update Employee Salary")
print("5.Generate Department Report")
print("6.Delete Employee")
print("7.Exit")

while True:
    choice=input("Enter your choice:")
    match choice:
        case '1':
            add_employee()
        case '2':
            display_all_employees()
        case '3':
            search_employee()
        case '4':
            update_sal()
        case '5':
            generate_report()
        case '6':
            delete_employee()
        case '7':
            print("Thankyou for entering the details")
            break

'''output:
----Employee Record Management----
1.Add New Employee
2.Display All Employees
3.Search Employee by ID
4.Update Employee Salary
5.Generate Department Report
6.Delete Employee
7.Exit

Enter your choice:1

E101,Neha Sharma,HR,60000,2020-05-10
E102,Ravi Kumar,IT,75000,2019-08-21
E103,Nisha,Finance,55000,2021-03-15
E104,Fatima Khan,HR,62000,2018-12-05
E105,Vikram Singh,Operations,58000,2022-01-11

Enter Employee ID:E106
Enter Name:Pranitha
Enter Department:Finance
Enter Salary:24000
Enter the joining:2018-10-06

Enter your choice:1
E101,Neha Sharma,HR,60000,2020-05-10
E102,Ravi Kumar,IT,75000,2019-08-21
E103,Nisha,Finance,55000,2021-03-15
E104,Fatima Khan,HR,62000,2018-12-05
E105,Vikram Singh,Operations,58000,2022-01-11
E106,Pranitha,Finance,24000.0,2018-10-06

Enter Employee ID:E107
Enter Name:Ram
Enter Department:HR   
Enter Salary:50000
Enter the joining:2024-12-12

Enter your choice:2
Employee Records:
E101 | Neha Sharma | HR | 60000 | 2020-05-10
E102 | Ravi Kumar | IT | 75000 | 2019-08-21
E103 | Nisha | Finance | 55000 | 2021-03-15
E104 | Fatima Khan | HR | 62000 | 2018-12-05
E105 | Vikram Singh | Operations | 58000 | 2022-01-11
E106 | Pranitha | Finance | 24000.0 | 2018-10-06
E107 | Ram | HR | 50000.0 | 2024-12-12

Enter your choice:3
Enter Employee ID to search: E106
Employee Found:
E106 | Pranitha | Finance | 24000.0 | 2018-10-06

Enter your choice:4
Enter Employee ID:106
Enter New Salary:100000
Salary is updated

Enter your choice:5
Report Generated

Enter your choice:6
Enter Employee ID to delete:102
Employee not found.

Enter your choice:7
Thankyou for entering the details
'''





                
