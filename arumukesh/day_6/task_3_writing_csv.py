import csv

emp_data=[[id,"name","department","salary"],
[101,"Arun","IT",70000],
[102,"Riya","HR",65000],
[103,"John","Finance",60000],
[104,"Neha","Marketing",55000]]

with open("employee_data02.csv","w",newline='')as file:
    csv_writer=csv.writer(file)
    
    csv_writer.writerows(emp_data)


