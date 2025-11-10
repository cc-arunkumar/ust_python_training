# Importing all parts
from part1_welcome import welcome_message
from part2_efficiency import calculate_efficiency
from part3_report import print_employee_report
from part4_project import get_active_project
from part5_team_average import scores

welcome_message()
print("Current Active Project:", project(), "\n")

eff1 = efficiency_score(26, 10)
eff2 = efficiency_score(20, 10)
eff3 = efficiency_score(20, 14)

report("Asha", "Finance", eff1)
report("Rahul", "IT", eff2)
report("Sneha", "HR", eff3)

scores(eff1, eff2, eff3)

#Sample output

# Welcome to UST Employee Work Report System
# This program helps HR calculate employee performance easily

# Current Active Project: UST Cloud Migration

# Employee: Asha | Department: Finance | Efficiency: 26.0
# Excellent performance

# Employee: Rahul | Department: IT | Efficiency: 20.0
# Good performance

# Employee: Sneha | Department: HR | Efficiency: 14.3
# Needs improvement

# Average Team Efficiency: 20.1
# Team needs improvement
