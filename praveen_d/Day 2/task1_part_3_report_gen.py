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


def report_generator(employee_name,department_name,employee_effiency_score):
    print(f"Employee name:{employee_name}")
    print(f"Employee department:{department_name}")
    print(f"Employee Efficiency score:{employee_effiency_score}")
    if employee_effiency_score>25:
        print("Excelent performance")
    elif employee_effiency_score<25 and employee_effiency_score>15:
        print("Good perfomance")
    else:
        print("Needs Improvement")

# function


