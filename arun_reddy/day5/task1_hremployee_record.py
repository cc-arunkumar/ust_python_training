# HR Employee Records

with open("employees.txt","w") as file:
    file.write("E101,Neha Sharma,HR,60000,2020-05-10 \n")
    file.write("E102,Ravi Kumar,IT,75000,2019-08-21 \n")
    file.write("E103,Arjun Mehta,Finance,55000,2021-03-15 \n")
    file.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
    file.write("E105,Vikram Singh,Operations,58000,2022-01-11")

while True:
    print("==== Employee Record Management ====")
    print("1. Add New Employee")
    print("2. Display All Employees")
    print("3. Search Employee by ID")
    print("4. Update Employee Salary")
    print("5. Generate Department Report")
    print("6. Delete Employee")
    print("7. Exit")
    num=int(input("Enter your choice:"))
    match num:
        case 1:
            name=input("Enter your name")
            id=input("Enter your id")
            dept=input("Enyter your department")
            sal=input("Enter your salary")
            joindate=input("Enter your date of joing")
            print("Employee added successfully")
            with open("employees.txt","a") as file:
                file.write(f"\n {id},{name},{dept},{sal},{joindate}")
        case 2:
            with open("employees.txt","r") as file:
                print("Employees Records:")
                for line in file:
                    str1=""
                    for ch in line:
                        if ch==',':
                            str1+=ch
                        else:
                            str1+=ch
                    print(str1)
        case 3:
            reqid=input("Enter ur employee id number:")
            with open("employees.txt","r") as file:
                for line in file:
                    if reqid in line:
                        print("Employee found:")
                        print(line.strip())
        case 4:
            id=input("Enter your id")
            sal=input("ENter your new salary")
            with open("employees.txt","r+") as file:
                lines=file.readlines()
                file.seek(0)
                for line in lines:
                    list1=line.strip().split(',')
                    if list1[0]==id:
                        list1[3]=sal
                        s=','.join(list1)+"\n"
                        file.write(s)
                    else:
                        file.write(line)
                file.truncate()
            with open("employees.txt","r") as file:
                for line in file:
                    print(line.strip())
        case 5:
            my_dict={}
            with open("employees.txt","r") as file:
                for line in file:
                    newlist=line.strip().split(',')
                    dept=newlist[2]
                    sal=int(newlist[3])
                    if my_dict.get(dept):
                        detail=my_dict[dept]
                        detail[0]+=1
                        detail[1]+=sal
                    else:
                        my_dict[newlist[2]]=[1,sal]
            with open("report.txt","w",encoding="utf-8") as file:
                for key,values in my_dict.items():
                    file.write(f"{key} Department → Employees: {values[0]} | Total Salary: {values[1]} | Average Salary: {values[1]/values[0]} \n")
        
        case 6:
            id=input("Enter ur id for deleting the record")
            with open("employees.txt","r+") as file:
                lines=file.readlines()
                for line in lines:
                    list2=line.strip().split(',')
                    if id==list2[0]:
                        print("Employee deleted succesfully")
                        pass
                    else:
                        strs=','.join(list2)+'\n'
                        file.write(strs)
                    file.truncate()
            with open("employees.txt","r") as file:
                for line in file:
                    print(line.strip())
        case 7:
            print("Exited Gracefully")
            break
            


# # sample Execution 
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees     
# 3. Search Employee by ID     
# 4. Update Employee Salary    
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice:1
# Enter your nameArunReddy
# Enter your idE110
# Enyter your departmentHR
# Enter your salary45000
# Enter your date of joing7-9-80
# Employee added successfully
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice:2
# Employees Records:
# E101,Neha Sharma,HR,60000,2020-05-10

# E102,Ravi Kumar,IT,75000,2019-08-21

# E103,Arjun Mehta,Finance,55000,2021-03-15

# E104,Fatima Khan,HR,62000,2018-12-05

# E105,Vikram Singh,Operations,58000,2022-01-11

#  E110,ArunReddy,HR,45000,7-9-80
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice:3
# Enter ur employee id number:E102
# Employee found:
# E102,Ravi Kumar,IT,75000,2019-08-21
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice:4
# Enter your idE101
# ENter your new salary45000
# E101,Neha Sharma,HR,45000,2020-05-10
# E102,Ravi Kumar,IT,75000,2019-08-21
# E103,Arjun Mehta,Finance,55000,2021-03-15
# E104,Fatima Khan,HR,62000,2018-12-05
# E105,Vikram Singh,Operations,58000,2022-01-11
# E110,ArunReddy,HR,45000,7-9-80
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice:5
# ==== Employee Record Management ====
# 1. Add New Employee
# 2. Display All Employees
# 3. Search Employee by ID
# 4. Update Employee Salary
# 5. Generate Department Report
# 6. Delete Employee
# 7. Exit
# Enter your choice:6
# HR Department → Employees: 2 | Total Salary: 122000 | Average Salary: 61000.0 
# IT Department → Employees: 1 | Total Salary: 75000 | Average Salary: 75000.0 
# Finance Department → Employees: 1 | Total Salary: 55000 | Average Salary: 55000.0 
# Operations Department → Employees: 1 | Total Salary: 58000 | Average Salary: 58000.0 


            

        
    
            