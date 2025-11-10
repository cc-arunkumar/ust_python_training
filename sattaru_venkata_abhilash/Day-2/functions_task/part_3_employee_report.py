# Part 3: Function with arguments and without return
# Objective:
# Display a formatted employee performance report.
# Takes employee name, department name, and efficiency score as inputs.
# Prints the report directly without returning any value.

def formatted_report(Employee_Name, Department_Name, efficiency_score):
    print(f"Employee: {Employee_Name} | Department: {Department_Name} | Efficiency: {efficiency_score:.1f}")
    
    if efficiency_score > 25:
        print("Excellent performance.")
    elif 15 <= efficiency_score <= 25:
        print("Good performance.")
    else:
        print("Needs improvement.")


# Sample Output:
# >>> formatted_report("Asha", "Finance", 26.0)
# Employee: Asha | Department: Finance | Efficiency: 26.0
# Excellent performance.
#
# >>> formatted_report("Rahul", "IT", 20.0)
# Employee: Rahul | Department: IT | Efficiency: 20.0
# Good performance.
#
# >>> formatted_report("Sneha", "HR", 14.3)
# Employee: Sneha | Department: HR | Efficiency: 14.3
# Needs improvement.
