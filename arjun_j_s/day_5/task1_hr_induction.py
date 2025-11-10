import os
ch='Y'
while(ch=='Y' or ch=='y'):
    print("==== Employee Record Management ====")
    print("1. Add New Employee")
    print("2. Display All Employees")
    print("3. Search Employee by ID")
    print("4. Update Employee Salary")
    print("5. Generate Department Report")
    print("6. Delete Employee")
    print("7. Exit")
    n=int(input("Choose choice:"))
    if(n==1):
        emp_name = input("Enter Name : ")
        emp_dep = input("Enter Department : ")
        emp_sal = int(input("Enter Salary : "))
        emp_join_date = input("Enter Joining Date (YYYY-MM-DD) : ")
        test = open("emp.txt","r")
        count=len(test.readlines())
        test.close()
        with open("emp.txt","a") as file:
            file.write(f"E0{count+1} {emp_name} {emp_dep} {emp_sal} {emp_join_date}\n")
            count+=1
        file.close()
        print("Added Successfully")
    elif(n==2):
        if(os.path.isfile("emp.txt")):
            with open("emp.txt","r") as file:
                d=file.readlines()
                if(len(d)>0):
                    for i in d:
                        data = i.strip().split(" ")
                        try:
                            print(f"{data[0]} | {data[1]} | {data[2]} | {data[3]} | {data[4]}")
                        except IndexError:
                            pass
                else:
                    print("No employees!!")
            file.close()
        else:
            print("File not found!!")                  
    elif(n==3):
        emp_id = input("Enter the employee id : ")
        if(os.path.isfile("emp.txt")):
            with open("emp.txt","r") as file:
                flag=0
                d=file.readlines()
                if(len(d)>0):
                    for i in d:
                        data = i.strip().split(" ")
                        if(len(data)>0 and data[0]==emp_id):
                            print("Employee Record : ")
                            flag=1
                            print(f"{data[0]} | {data[1]} | {data[2]} | {data[3]} | {data[4]}")
                            break
                    if(flag==0):
                        print("Not found!!")
                else:
                    print("Not found!!")
        else:
            print("File not found!!")   
    elif(n==4):
        emp_id = input("Enter the employee id : ")
        sal = int(input("Enter the salary : "))
        if(os.path.isfile("emp.txt")):
            with open("emp.txt","r") as file:
                d=file.readlines()
                if(len(d)>0):
                    for i in range(len(d)):
                        data = d[i].strip().split(" ")
                        if(data[0]==emp_id):
                            d[i]=f"{data[0]} {data[1]} {data[2]} {sal} {data[4]}\n"
                            break
            with open("emp.txt","w") as file:   
                file.writelines(d)
                print("Update Successfull!!")
        else:
            print("File not found!!") 

    elif(n==5):
        dic={}
        file = open("emp.txt","r")
        d=file.readlines()
        for j in d:
            data = j.strip().split(" ")
            if(data[2] not in dic):
                dic[data[2]]={"emp":0,"total_sal":0,"avg_sal":0}
            dic[data[2]]["emp"]+=1
            dic[data[2]]["total_sal"]+=int(data[3])
            dic[data[2]]["avg_sal"]=round(dic[data[2]]["total_sal"]/dic[data[2]]["emp"],2)
        with open("report.txt","w") as new:
            for i in dic:
                new.write(f"{i} Department -> Employees {dic.get(i)["emp"]} | Total {dic.get(i)["total_sal"]} | Average {dic.get(i)["avg_sal"]}\n")
        print("Generated!!")
        new.close()
        with open("report.txt","r") as new:
            out=new.read()
        print(out)
        new.close()
        file.close()
    elif(n==6):
        emp_id = input("Enter the employee id : ")
        if(os.path.isfile("emp.txt")):
            with open("emp.txt","r") as file:
                d=file.readlines()
                if(len(d)>0):
                    for i in range(len(d)):
                        data = d[i].strip().split(" ")
                        if(data[0]==emp_id):
                            d.pop(i)
                            break
            with open("emp.txt","w") as file:   
                file.writelines(d)
                print("Deleted Successfull!!")
        else:
            print("File not found!!") 
    elif(n==7):
        print("Thank you! Have a great day.")
        break
    else:
        print("Provide a number within range!!")
    ch=input("\nDo you wish to continue(Y/N)")

#Output
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Choose choice:1
# Enter Name : Ravi
# Enter Department : IT
# Enter Salary : 30000
# Enter Joining Date (YYYY-MM-DD) : 2025-02-23
# Added Successfully

# Do you wish to continue(Y/N)y
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Choose choice:2
# E01 | Arjun | HR | 10000 | 2025-11-03
# E02 | Rahul | HR | 10000 | 2025-11-02
# E03 | Biju | IT | 20000 | 2025-04-11
# E04 | Ravi | IT | 30000 | 2025-02-23

# Do you wish to continue(Y/N)y
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Choose choice:3
# Enter the employee id : E01
# Employee Record : 
# E01 | Arjun | HR | 10000 | 2025-11-03

# Do you wish to continue(Y/N)y
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Choose choice:4
# Enter the employee id : E01
# Enter the salary : 12000
# Update Successfull!!

# Do you wish to continue(Y/N)y
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Choose choice:5
# Generated!!
# HR Department -> Employees 2 | Total 22000 | Average 11000.0
# IT Department -> Employees 2 | Total 50000 | Average 25000.0


# Do you wish to continue(Y/N)y
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Choose choice:6
# Enter the employee id : E04
# Deleted Successfull!!

# Do you wish to continue(Y/N)n