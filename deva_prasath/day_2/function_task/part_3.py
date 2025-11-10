def employee_details(name,dept,efficiency):
    print(f"Employee: {name} | Department: {dept} | Efficiency: {efficiency:.1f}")
    
    if efficiency > 25:
        print("Excellent performance.")
    elif 15 <= efficiency <= 25:
        print("Good performance.")
    else:
        print("Needs improvement.")
