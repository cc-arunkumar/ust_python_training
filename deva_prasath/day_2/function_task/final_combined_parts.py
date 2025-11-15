# UST Employee DailyWork Report Automation
# After collecting data from multiple employees, HR wants to know the average
# efficiency score of the entire team.

# Import necessary functions from different modules
from part_1 import greet_msg
from part_2 import calculate_efficiency
from part_3 import employee_details
from part_4 import active_project
from part_5 import team_average_efficiency

# Call greet_msg function to display a greeting message
greet_msg()

# Get and display the current active project
project = active_project()
print(f"Current Active Project: {project}")

# Calculate efficiency for each employee (using hypothetical values for tasks and time)
deva_eff = calculate_efficiency(21, 8)
prasath_eff = calculate_efficiency(20, 10)
varun_eff = calculate_efficiency(20, 14)

# Display employee details and performance evaluation
employee_details("Deva", "IT", deva_eff)
employee_details("Prasath", "CSE", prasath_eff)
employee_details("Varun", "HR", varun_eff)

# Calculate and display the average team efficiency
team_average_efficiency(deva_eff, prasath_eff, varun_eff)


#Sample output

# Welcome to UST Employee Work Report System. 
# This program helps HR calculate employee perfomance easily.
# Welcome to UST Employee Work Report System.
# This program helps HR calculate employee perfomance easily.
# Current Active Project: UST Cloud Migration
# Employee: Deva | Department: IT | Efficiency: 26.2
# Excellent performance.
# Employee: Prasath | Department: CSE | Efficiency: 20.0
# Good performance.
# Employee: Varun | Department: HR | Efficiency: 14.3
# Needs improvement.
# Average Team Efficiency: 20.178571428571427
# Team needs improvement.