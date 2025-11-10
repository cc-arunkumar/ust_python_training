from task2 import efficiency_score

def formatted_report(employee_name,department_name,efficiency_score):
    print("Employee : ",employee_name,"|",end="")
    print("Deparment: ",department_name,"|",end="")
    print("Efficience :",efficiency_score)
    if(efficiency_score>25):
        print("Excellent performance.")
    elif(efficiency_score>15):
        print("Good performance.")
    else:
        print("Needs improvement.")

efficiency = efficiency_score(10,29)
formatted_report("Asha","Finance",efficiency)

efficiency = efficiency_score(9,10)
formatted_report("Rahul","IT",efficiency)

efficiency = efficiency_score(7,6)
formatted_report("Sneha","HR",efficiency)

# output

# Employee :  Asha |Deparment:  Finance |Efficience : 29.0
# Excellent performance.
# Employee :  Rahul |Deparment:  IT |Efficience : 11.11111111111111
# Needs improvement.
# Employee :  Sneha |Deparment:  HR |Efficience : 8.571428571428571
# Needs improvement.