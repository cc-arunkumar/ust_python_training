
def report(emp_name,dept_name,efficiency_score):
    print(f"Employee: {emp_name} , | Department: {dept_name} , | Efficiency: {efficiency_score}" )
    if(efficiency_score>25):
        print("Excellent Performance")
    elif(efficiency_score>=15 or efficiency_score<=25):
        print("Good Performance")
    else:
        print("Needs improvement")
