import os

#takes the input from user
def takeinput():
    empid=input("Enter Employee ID: ")
    empname=input("Enter Name: ")
    empdep=input("Enter Department: ")
    empsalary=int(input("Enter Salary: "))
    empjoindate=input("Enter Joining Date (YYYY-MM-DD): ")
    
    flag=True
    with open("employees.txt","r") as f:
        for line in f:
            li=line.strip().split(",")
            if empid==li[0]:
                flag=False
                break
            
    if flag:
        with open("employees.txt","a") as f:
            f.write(f"\n{empid},{empname},{empdep},{empsalary},{empjoindate}")
            print("Employee Added Succesfully")
    else:
        print("Employee Already exist")
        
#Displays all employees         
def displayall():
    if os.path.exists("employees.txt"):
        print("Employee Records: ")
        with open("employees.txt","r") as f:
            for line in f:
                x=line.strip().split(",")
                print("|".join(x))
    else:
        print("No employee Records found")   

#Search specific Employee
def search():
    searchid=input("Enter Employee ID to search: ")
    with open("employees.txt","r") as f:
        flag=False
        for l in f:
            line=l.split(",")
            id=line[0]
            if(searchid==id):
                print("Employee Found: ")
                print("|".join(line))
                flag=True
                break
                
    if not flag:
        print("Employee Not Found")
    return

#Update salary of employee
def updateemp():
    id=input("Enter Employee ID: ")
    updatedsalary=int(input("Enter New Salary: "))
    content=[]
    with open("employees.txt","r") as f:
        for line in f:
            content.append(line)
            
    with open("employees.txt","w") as f:
        for line in content:
            li=line.split(",")
            if li[0]==id:
                f.write(f"{li[0]},{li[1]},{li[2]},{updatedsalary},{li[4]}")
            else:
                f.write(line)
    
#Delete employee data
def deleteemp():
    id=input("Enter Employee ID to delete: ")
    content=[]
    with open("employees.txt","r") as f:
        for line in f:
            content.append(line)
            
    with open("employees.txt","w") as f:
        for line in content:
            li=line.split(",")
            if li[0]==id:
                print("Employee deleted successfully!")
                continue
            else:
                f.write(line)
    
#department wise report
def departmentwise():
    dic={}
    with open("employees.txt","r") as f:
        for line in f:
            emp=line.split(",")
            if emp[2] in dic.keys():
                dic[emp[2]].append(float(emp[3]))
            else:
                dic[emp[2]]=[float(emp[3])]
    with open("report.txt","w") as f:
        for key,value in dic.items():
            f.write(f"\n{key} Department -> Employees: {len(value)}| Total Salary: {sum(value)}| Average Salary: {sum(value)/len(value)}")
            
                    
            
    

print("==== Employee Record Management ====")
print("1. Add New Employee")
print("2. Display All Employees")
print("3. Search Employee by ID")
print("4. Update Employee Salary")
print("5. Generate Department Report")
print("6. Delete Employee")
print("7. Exit")

while(True):
    n=int(input("Enter your choice: "))
    if n==1:
        takeinput()
        print()
        
    elif n==2:
        displayall()
        print()
        
    elif n==3:
        search()
        print()
        
    elif n==4:
        updateemp()
        print()
        
    elif n==5:
        departmentwise()
        print()
        
    elif n==6:
        deleteemp()
        print()
        
    elif n==7:
        print("Exited Successfully!")
        break;
    else:
        print("Enter Valid Choice")
    
           
         
#==== Employee Record Management ====
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
# Enter Department: HR
# Enter Salary: 59000
# Enter Joining Date (YYYY-MM-DD): 2022-11-20
# Employee Added Succesfully

# Enter your choice: 2
# Employee Records: 
# E101|Neha Sharma|HR|60000|2020-05-10
# E102|Ravi Kumar|IT|75000|2019-08-21
# E103|Arjun Mehta|Finance|55000|2021-03-15
# E104|Fatima Khan|HR|59000|2018-12-05
# E105|Vikram Singh|Operations|58000|2022-01-11


# E106|Meera Nair|HR|59000|2022-11-20

# Enter your choice: 3
# Enter Employee ID to search: E104
# Employee Found: 
# E104|Fatima Khan|HR|59000|2018-12-05


# Enter your choice: 4
# Enter Employee ID: E104
# Enter New Salary: 64000

# Enter your choice: 5

# Enter your choice: 6
# Enter Employee ID to delete: E106
# Employee deleted successfully!

# Enter your choice: 7
# Exited Successfully!