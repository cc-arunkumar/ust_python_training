employee=open("employeedata.txt",'r')
search="E105"
found=False
for line in employee:
    parts=line.strip().split(',')
    if len(parts)==5:
        emp_id,emp_name,emp_dept,emp_sal,emp_joing=parts
        if emp_id==search:
            print("employee found")
            print(f"{emp_id}|{emp_name}|{emp_dept}|{emp_sal}|{emp_joing}")
            found=True
            break
employee.close()
if not found:
    print("employee data not found")
    
    
# output  
# employee found
# E105|Vikram Singh|Operations|58000|2022-01-11