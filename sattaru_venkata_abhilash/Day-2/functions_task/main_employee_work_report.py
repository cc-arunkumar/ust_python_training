# Day 2: UST Employee Daily Work Report Automation
# Main Program
# -----------------------------------------------------
# This program automates employee performance tracking using
# modular functions imported from separate files:
# 1. part_1_welcome.py  → Function without arguments & without return
# 2. part_2_efficiency.py → Function with arguments & with return
# 3. part_3_employee_report.py → Function with arguments & without return
# 4. part_4_project_name.py → Function without arguments & with return
# 5. part_5_average.py → Function with variable arguments (*args)
# -----------------------------------------------------

from part_1_welcome import welcome_message
from part_2_efficiency import efficiency_score
from part_3_employee_report import formatted_report
from part_4_project_name import project_name
from part_5_average import average_efficiency_score

# Part 1: Welcome message
welcome_message()

# Part 4: Display current project name
print(project_name())

# Part 2: Calculate efficiency scores
efficiency_1 = efficiency_score(10, 11)
efficiency_2 = efficiency_score(8, 9)
efficiency_3 = efficiency_score(4, 8)

# Part 3: Display individual employee reports
formatted_report("Asha", "Finance", efficiency_1)
formatted_report("Rahul", "IT", efficiency_2)
formatted_report("Sneha", "HR", efficiency_3)

# Part 5: Display team average performance
average_efficiency_score(efficiency_1, efficiency_2, efficiency_3)





# OverAll Output:
# Welcome to UST Employee Work Report System
# This program helps HR calculate employee performance easily.
# Current Active Project: UST Cloud Migration
# Employee: Asha | Department: Finance | Efficiency: 11.0
# Needs improvement.
# Employee: Rahul | Department: IT | Efficiency: 11.2
# Needs improvement.
# Employee: Sneha | Department: HR | Efficiency: 20.0
# Good performance.
# Average Team Efficiency: 14.1
# Team needs improvement.
