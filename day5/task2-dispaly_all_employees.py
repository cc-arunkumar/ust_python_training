# Display All Employees

file3=open("employeedata.txt",'r')
for line in file3:
    
    parts = line.strip().split(',')
    if len(parts) == 5:
        emp_id,emp_name,emp_dept,emp_sal,emp_joing=parts
        print(f"{emp_id}|{emp_name}|{emp_dept}|{emp_sal}|{emp_joing}")
        
        
# E101|Neha Sharma|HR|60000|2020-05-10
# E102|Ravi Kumar|IT|75000|2019-08-21
# E103|Arjun Mehta|Finance|55000|2021-03-15
# E104|Fatima Khan|HR|62000|2018-12-05
# E105|Vikram Singh|Operations|58000|2022-01-11
# E106|Meera Nair|HR|64000|2022-11-20
        