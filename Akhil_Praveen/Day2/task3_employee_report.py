from task2_employee_efficiency import employee_efficiency

def employee_report(name,dept,efficiency):
    print("Employee name: ",name)
    print("Department name: ",dept)
    if(efficiency>25):
        print("Excellent performance.")
    elif(efficiency>15 and efficiency<25):
        print("Good performance.")
    else:
        print("Needs improvement.")
    
efficiency=employee_efficiency(10,5)
employee_report("Asha","Finance",efficiency)
efficiency=employee_efficiency(8,6)
employee_report("Rahul","IT",efficiency)
efficiency=employee_efficiency(6,9)
employee_report("Akhil","Developer",efficiency)
# Employee name:  Asha
# Department name:  Finance
# Needs improvement.
# Employee name:  Rahul
# Department name:  IT
# Needs improvement.
# Employee name:  Akhil
# Department name:  Developer
# Needs improvement.