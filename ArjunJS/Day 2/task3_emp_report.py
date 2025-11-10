def emp_report(emp_name,emp_dep,eff_score):
    print(f"Employee Name : {emp_name}")
    print(f"Department : {emp_dep}")
    print(f"Efficiency : {eff_score}")
    if(eff_score>25):
        print("Excellent Performance")
    elif(15<=eff_score<=25):
        print("Good Performance")
    else:
        print("Need Improvement")