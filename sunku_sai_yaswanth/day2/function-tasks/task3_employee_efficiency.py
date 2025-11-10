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
# This function should not return any value — it only displays output


def employee(ename,dname,efficiency):
    print("Name:",ename)
    print("dname:",dname)
    if(efficiency>25):
        print("excellent")
    elif(efficiency >15 and efficiency<25):
        print("good performanse")


employee("sai","cse",45)



#Name: sai
# dname: cse
# excellent