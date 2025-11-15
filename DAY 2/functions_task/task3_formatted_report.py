"""
Objective:
After calculating the efficiency, HR wants to print a formatted report for each employee.

Requirements:
Create a function that takes 3 inputs:
Employee Name
Department Name
Efficiency Score (calculated from the previous function)
Inside the function:
Print the employee’s details in a clean, readable format.
If efficiency is greater than 25, print:
“Excellent performance.”
If efficiency is between 15 and 25, print:
“Good performance.”
Otherwise, print:
“Needs improvement.”
This function should not return any value — it only displays output.


"""


def calculate_efficiney_score(tasks_completed,hrs_worked):   # Function to calculate efficiency score
    Efficiency=(tasks_completed/hrs_worked)*10   # Compute efficiency using formula
    return Efficiency   # Return the score to caller


def calculate_efficiency(emp_name,dep_name,eff_score):   # Function to display employee report
    if eff_score>25:   # Check if efficiency >25
        print("Excellent Performance")   # Print excellent performance
    elif eff_score>15:   # Check if efficiency between 15 and 25
        print("Good Peformance")   # Print good performance
    else : print("Needs Improvement")   # Print needs improvement for lower efficiency

emp_name=input("Enter name: ")   # Input employee name
dep_name=input("Enter Department: ")   # Input department name
tasks_completed=int(input("Enter Taks COmpleted: "))   # Input tasks completed
hrs_worked=int(input("Total Hours Worked: "))   # Input hours worked

eff_score=calculate_efficiney_score(tasks_completed,hrs_worked)   # Calculate efficiency

calculate_efficiency(emp_name,dep_name,eff_score)   # Display employee report


# SAMPLE OUTPUT

"""Enter name: Gowtham
Enter Department: IT
Enter Taks COmpleted: 10
Total Hours Worked: 2
Excellent Performance"""
