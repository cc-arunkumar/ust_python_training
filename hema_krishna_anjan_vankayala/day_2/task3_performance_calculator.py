#Part 3: Function with arguments and without return

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

def overview_performance(name,department,efficiency_score):
    print(f"Employee: {name} | Department: {department} | Efficiency: {efficiency_score}")
    if efficiency_score>=25:
        print("Excellent performance")
    elif efficiency_score>=15 and efficiency_score<25:
        print("Good performance")
    else:
        print("Needs improvement")

#Sample Output
#overview_performance("John Doe","IT",18.75)
#Employee: John Doe | Department: IT | Efficiency: 18.75
#Good performance