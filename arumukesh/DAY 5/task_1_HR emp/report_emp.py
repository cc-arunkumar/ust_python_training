def report():

    emp_dept={}
    emp_l=[]
    emp_unique=set()

    with open("employees.txt","r") as file:
        for line in file:
            details=line.strip().split(",")
            emp_unique.add(details[0])
    with open("employees.txt","r") as files:
        
        for lines in files:
            details=lines.strip().split(",")
            # emp_l.append(",".join(details),"\n")
            emp_id,name,dept,salary,date=details
            salary=float(salary)
            if dept not in emp_dept:
                emp_dept[dept]=[0,0.0]
            emp_dept[dept][0]+=1
            emp_dept[dept][1]+=salary
    for key,values in emp_dept.items():
        print(f"Department:{key} |No. Of employees:{values[0]}| Total Salary:{values[1]}| average salary:{values[1]/values[0]}")


report()


            