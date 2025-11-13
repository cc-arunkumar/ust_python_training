employee=open("employeedata.txt",'w')
employee.write("E101,Neha Sharma,HR,60000,2020-05-10\n")
employee.write("E102,Ravi Kumar,IT,75000,2019-08-21\n")
employee.write("E103,Arjun Mehta,Finance,55000,2021-03-15\n")
employee.write("E104,Fatima Khan,HR,62000,2018-12-05\n")
employee.write("E105,Vikram Singh,Operations,58000,2022-01-11\n")

file_name="employeedata.txt"
search_data="E106"
found=False
for line in file_name:
    if search_data in line:
        print(f"search_data {search_data} is found {line.strip()}")
        foud=True
if not found:
    print("not found")
    

# emp_id=input("enter the emp_id: ")
# emp_name=input("enter the emp_name: ")
# emp_dept=input("enter the employee dept: ")
# emp_sal=input("enter the employee sal:")
# emp_dateofjoing=input("enter the joing:")
employee=open("employeedata.txt",'a')
employee.write("E106,Meera Nair,HR,64000,2022-11-20")
employee.close()
print("employee record added")

    
