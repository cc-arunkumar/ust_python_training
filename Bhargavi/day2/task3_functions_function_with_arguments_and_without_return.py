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


# Function to calculate efficiency score

def score(task_completed, hours_worked):
    return (task_completed / hours_worked) * 10

# Function to print formatted employee report
def formated_report(emp_name, dept_name, eff_score):
    print("Employee Name:", emp_name)
    print("Department Name:", dept_name)
    print("Efficiency Score:", round(eff_score, 2))  # rounded to 2 decimals
    
    # Performance evaluation based on efficiency score
    if eff_score > 25:
        print("Excellent performance")
    elif 15 <= eff_score <= 25:
        print("Good performance")
    else:
        print("Needs improvement")

# Collect input from user
name = input("Enter employee name: ")
dept = input("Enter department name: ")
tasks = int(input("Enter tasks completed: "))
hours = float(input("Enter hours worked: "))

# Calculate efficiency score
eff = score(tasks, hours)

# Generate formatted report
formated_report(name, dept, eff)


# output:
# Enter employee name: Bhargavi S
# Enter department name: Devlopment
# Enter tasks completed: 30
# Enter hours worked: 20
# Employee Name: Bhargavi S
# Department Name: Devlopment
# Efficiency Score: 15.0
# Good performance
