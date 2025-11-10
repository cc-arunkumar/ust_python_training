from ntpath import join
import os

with open("employees.txt","w") as file:
    file.write("E101,Neha Sharma,HR,60000,2020-05-10\n")
    file.write("E102,Ravi Kumar,IT,75000,2019-08-21\n")
    file.write("E103,Arjun Mehta,Finance,55000,2021-03-15\n")
    file.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
    file.write("E105,Vikram Singh,Operations,58000,2022-01-11\n")
    
# emp_id=input("Enter Employee ID:")
# name=input("Enter Name:")
# depatment_name=input("Enter Department:")
# salary=input("Enter Salary:")
# date=input("Enter Joining Date (YYYY-MM-DD):")

# new_record=emp_id+","+name+","+depatment_name+","+salary+","+date
# flag=False
# with open("employees.txt","r") as file:
#     for line in file:
#         existing=line.strip().split(",")[0]
#         if existing==emp_id:
#             flag=True
#             break

# if flag:
#     print("File already exists")
# else:
with open("employees.txt","a") as file:
    file.write("E106,Meera Nair,HR,64000,2022-11-20")

with open("employees.txt","r") as file:
    content=file.read().splitlines()
    for line in content:
        data=line.split(",")
        print("|".join(data))
# emp_id=input("Enter Employee ID to search:")

# flag=False
# with open ("employees.txt","r") as file:
#     # line=file.read().split(",")
#     for line in file:
#         lines=line.split(",")
#         if lines[0]==emp_id:
#             print(f"{line[0]}, {line[1]}, {line[2]} , {line[3]}, {line[4]}")
#             flag=Truebreak
# if not flag:
#     print("Employee not found")    
dict={}
data=[]
with open("employees.txt","r") as file:
    for line in file:
        lines=line.strip().split(",")
        emp_id,name,dept,salary,date=lines
        data.append(lines)
        salary=float(salary)
        
        if dept not in data:
            dict[dept]={"count":0,"total":0}
        dict[dept]["count"]+=1
        dict[dept]["total"]+=salary
        
        
with open("reports.txt","w") as report:
    for line,val in dict.items():
        count=val["count"]
        total=val["total"]
        average=total/count
        
        report_line=f"{dept} Department -> Employees: {count} | Total Salary: {total} | Average salary: {average:.1f}\n "
        report.write(report_line)        
        
emp_id="E104"

with open("employees.txt","r") as file:
    lines=file.readlines()
    
flag=False

with open("employees.txt","w") as file:
    for line in lines:
        if line.startswith(emp_id+","):
            flag=True
            continue
        file.write(line)
if flag:
    print("Employee deleted successfully!")
else:
    print("Employee Not found")
        

