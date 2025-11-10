#Task 1 : File Handling 

file = open("employees.txt", "w")
file.write("E101,NehaSharma,HR,60000,2020-05-10,")
file.write("E102,Ravi Kumar, IT,750000,2019-08-21,")
file.write("E103,Arjun Mehta, Finance,55000,2021-01-15,")
file.write("E104,Fatima Khan,HR,62000,2018-12-15,")
file.write("E105, Vikram Singh,Operation,58000,2022-01-11,")
file.close()

def add_employee():
    existing_id=set()
    with open("employees.txt","r") as f:
        for line in f:
            parts=line.strip().split(",")
            if parts:
                existing_id.add(parts[0])
    emp_id=input("Enter the user id : ")
    if emp_id in existing_id:
        print("Error employee id already exixts")
        return
    name = input("Enter your name : ")
    dept = input("Enter yout dept : ")
    sal = input("Enter your salary : ")
    doj = input("Enter your date of Joining : ")
    
    record= f"{emp_id},{name},{dept},{sal},{doj}\n"
    with open("employees.txt","a") as f:
        f.write(record)
    print("Record added something")
    
def display_all():
    with open("employees.txt","r") as f:
        print("======Employee Records======")
        for line in f:
            print(line.strip())


def search_employee():
    emp_id=input("Enter the Employee ID: ")
    found =False
    with open("employees.txt", "r") as f:
        for line in f:
            parts=line.strip().split(", ")
            if parts[0]==emp_id:
                print("Employee Found : ",line.strip())
                found=True
                break
    if not found:
        print("Employee Not found ")
           
def update_sal():
    emp_id=input("Enter the employee id : ")
    new_sal=input("Enter the new sal : ")
    lines=[]
    updated = False
    with open("employees.txt","r") as f:
        lines=f.readlines()
    for i in range(len(lines)):
        parts=lines[i].strip().split(",")
        if parts[0]==emp_id:
            parts[3]=new_sal
            lines[i]=", ".join(parts) + "\n"
            updated=True
            break
    if updated:
        with open("employees.txt", "w") as file:
            file.writelines(lines)
    else:
        print("Employee Id not exixts")

def dept_report():
    dept_summary={}
    with open("employees.txt","r") as f:
        for line in f:
            parts=line.strip().split(", ")
            dept=parts[2]
            sal= int(parts[3])
            if dept not in dept_summary:
                dept_summary[dept]={"Count ": 0, "Total salary": 0}
                dept_summary[dept]["count"]+=1
                dept_summary[dept]["Total salary"]+=sal
    print("Department Report")
    for dept,data in dept_summary.items():
        avg_sal= data["Total salary"]/ data["count"]
        print()
def delete_employee():
    emp_id = input("Enter the ID: ")
    lines=[]
    deleted=False
    with open("employees.txt","r") as f:
        lines=f.readlines()
    new_lines =[]
    for line in lines:
        parts=line.strip().split(", ")
        if parts[0] == emp_id:
            deleted=True
            continue
        new_lines.append(line)
    if deleted:
        with open("employees.txt", "w") as f :
            f.writelines(new_lines)
            print("Employee Deleted sucessfully")
    else:
        print("Employee ID not found")
while True:
    print("1.Add new Employeee")
    print("2.Update Sal ")
    print("3.Search Employee")
    print("4.Delete Employee")
    print("5. Generate Department Report : ")
    print("6.Display Employee ")
    print("7. Exit")
    
    choice=int(input("Enter your choice : "))
    
    if choice ==1:
        add_employee()
    elif choice==2:
        update_sal()
    elif choice==3:
        search_employee()
    elif choice==4:
        delete_employee()
    elif choice==5:
        dept_report()
    elif choice==6:
        display_all()
    elif choice==7:
        print("Exit")
        break
    else:
        print("Invalid")
        
#Output
# 1.Add new Employeee
# 2.Update Sal 
# 3.Search Employee
# 4.Delete Employee
# 5. Generate Department Report : 
# 6.Display Employee 
# 7. Exit
# Enter your choice : 1
# Enter the user id : E106
# Enter your name : sohan
# Enter yout dept : IT
# Enter your salary : 340000
# Enter your date of Joining : 2025-01-20
# Record added something
# 1.Add new Employeee
# 2.Update Sal
# 3.Search Employee
# 4.Delete Employee
# 5. Generate Department Report :
# 6.Display Employee
# 7. Exit
# Enter your choice : 6
# ======Employee Records======
# E101,NehaSharma,HR,60000,2020-05-10,E102,Ravi Kumar, IT,750000,2019-08-21,E103,Arjun Mehta, Finance,55000,2021-01-15,E104,Fatima Khan,HR,62000,2018-12-15,E105, Vikram Singh,Operation,58000,2022-01-11,E106,sohan,IT,340000,2025-01-20
# 1.Add new Employeee
# 2.Update Sal
# 3.Search Employee
# 4.Delete Employee
# 5. Generate Department Report : 
# 6.Display Employee
# 7. Exit
# Enter your choice : 7
# Exit
        
    
            
        
    



        
    