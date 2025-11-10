def delete_emp():
    emp_id=input("enter EMP_ID: ")
    emp=[]
    with open("employees.txt","r") as files:
        for line in files:
            details=line.strip().split(",")
            if details[0]==emp_id:
                continue
            emp.append(",".join(details)+"\n")
    with open("employees.txt","w") as files:
        for det in emp:
            files.write(det)
    print("Item deleted")
delete_emp()
                