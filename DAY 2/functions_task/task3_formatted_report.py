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


def calculate_efficiney_score(tasks_completed,hrs_worked):
    Efficiency=(tasks_completed/hrs_worked)*10
    return Efficiency


def calculate_efficiency(emp_name,dep_name,eff_score):
    if eff_score>25:
        print("Excellent Performance")
    elif eff_score>15:
        print("Good Peformance")
    else : print("Needs Improvement")

emp_name=input("Enter name: ")
dep_name=input("Enter Department: ")
tasks_completed=int(input("Enter Taks COmpleted: "))
hrs_worked=int(input("Total Hours Worked: "))

eff_score=calculate_efficiney_score(tasks_completed,hrs_worked)

calculate_efficiency(emp_name,dep_name,eff_score)


# SAMPLE OUTPUT

"""Enter name: Gowtham
Enter Department: IT
Enter Taks COmpleted: 10
Total Hours Worked: 2
Excellent Performance"""