from part_1 import greet_msg
from part_2 import calculate_efficiency
from part_3 import employee_details
from part_4 import active_project
from part_5 import team_average_efficiency

greet_msg()

project = active_project()
print(f"Current Active Project: {project}")

deva_eff = calculate_efficiency(21, 8)
prasath_eff = calculate_efficiency(20, 10)
varun_eff = calculate_efficiency(20, 14)

employee_details("Deva", "IT", deva_eff)
employee_details("Prasath", "CSE", prasath_eff)
employee_details("Varun", "HR", varun_eff)

team_average_efficiency(deva_eff, prasath_eff, varun_eff)


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