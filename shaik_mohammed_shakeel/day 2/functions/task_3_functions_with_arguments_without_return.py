
# Task 3: Function with arguments and without return
# Day 2

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
# This function should not return any value — it only displays out

def report(Ename,Dname,Ec):
    print("Employee Name: ",Ename)
    print("Department Name: ",Dname)
    print("Efficiency: ",Ec)

    if(Ec>25):
        print("Excellent Performance")
    elif(15<Ec<=25):
        print("Good Performance")
    else:
        print("Need Improvement")

report("Rajeev","Developer",88)
report("sanjeev","HR",22)


#Sample Outputs

# Employee Name:  Rajeev
# Department Name:  Developer
# Efficiency:  88
# Excellent Performance
# Employee Name:  sanjeev
# Department Name:  HR
# Efficiency:  22
# Good Performance