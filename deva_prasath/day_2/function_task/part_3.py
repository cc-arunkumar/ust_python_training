# Function to display employee details and performance evaluation
def employee_details(name, dept, efficiency):
    # Print employee details
    print(f"Employee: {name} | Department: {dept} | Efficiency: {efficiency:.1f}")
    
    # Evaluate performance based on efficiency
    if efficiency > 25:
        print("Excellent performance.")
    elif 15 <= efficiency <= 25:
        print("Good performance.")
    else:
        print("Needs improvement.")
