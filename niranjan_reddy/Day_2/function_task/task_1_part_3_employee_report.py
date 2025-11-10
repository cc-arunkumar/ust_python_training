# Part 3: Function with arguments and without return

# Objective:
# After calculating the efficiency, HR wants to print a formatted report for each
# employee.

# Requirements:
# Create a function that takes 3 inputs:
# Employee Name
# Department Name
# Efficiency Score (calculated from the previous function)
# Inside the function:
# Print the employee’s details in a clean, readable format.
# If efficiency is greater than 25, print:
# “Excellent performance.”
# If efficiency is between 15 and 25, print:
# “Good performance.”
# Otherwise, print:
# “Needs improvement.”
# This function should not return any value — it only displays output.

def formatted_report(Employee_Name,Department_Name,efficiency_score ):
    print("Employee: ",Employee_Name,"| Department: ",Department_Name,"| Efficiency: ", efficiency_score)
    
    if efficiency_score >25:
        print("Excellent performance.")
    
    elif 15<=efficiency_score <=25:
        print("Good performance.")
    
    else:
        print("Needs improvement")
