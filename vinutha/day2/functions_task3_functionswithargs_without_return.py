# #Function with arguments and without return

# Part 3: Function with arguments and without return
# Day 2 2
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

#code

# Function to calculate efficiency score based on tasks completed and hours worked
def score(task_completed, hours_worked):
    return (task_completed / hours_worked) * 10   

# Function to print a formatted employee performance report
def formated_report(emp_name, dept_name, eff_score):
    print("Employee Name:", emp_name)            
    print("Department Name:", dept_name)         
    print("Efficiency Score:", round(eff_score, 2))  
    
    # Performance evaluation based on efficiency score
    if eff_score > 25:
        print("Excellent performance")
    elif 15 <= eff_score <= 25:
        print("Good performance")
    else:
        print("Needs improvement")

# Collect employee details and work data from user input
name = input("Enter employee name: ")
dept = input("Enter department name: ")
tasks = int(input("Enter tasks completed: "))
hours = float(input("Enter hours worked: "))

# Calculate efficiency score using the score function
eff = score(tasks, hours)

# Generate and display the formatted report
formated_report(name, dept, eff)


#output
# PS C:\Users\303379\day2_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day2_training/task3_functions.py
# Enter employee name: Vinnu
# Enter department name: developer
# Enter tasks completed: 18
# Enter hours worked: 100
# Employee Name: Vinnu
# Department Name: developer
# Efficiency Score: 1.8
# Needs improvement
# PS C:\Users\303379\day2_training> 