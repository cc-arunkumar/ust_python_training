# Function with arguments and without return

def print_employee_report(employee_name, department_name, efficiency):
    print(f"Employee: {employee_name} | Department: {department_name} | Efficiency: {efficiency:.1f}")
    if efficiency > 25:
        print("Excellent performance.\n")
    elif 15 <= efficiency <= 25:
        print("Good performance.\n")
    else:
        print("Needs improvement.\n")
