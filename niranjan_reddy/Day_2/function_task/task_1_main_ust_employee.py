# Task: UST Employee DailyWork Report Automation



# Background:
# UST managers maintain daily work reports for each employee.
# Every employee records:
# How many hours they worked,
# How many tasks they completed, and
# Their department name.
# The HR department wants a small Python program that helps them automate a
# few daily actions.
# You have been assigned to build this small program step-by-step using different
# kinds of Python functions.
# The goal of this exercise is not only to get the output but also to understand when
# and why we use:
# 1. Functions with arguments and return values
# 2. Functions without arguments but with return values
# 3. Functions with arguments but without return values
# 4. Functions without arguments and without return values
# 5. Functions with variable arguments ( args )




from task_1_part_1_welcome import welcome_message
from task_1_part_2_efficiency import efficiency_score
from task_1_part_3_employee_report import formatted_report
from task_1_part_4_project_name import project_name
from task_1_part_5_average import average_efficiency_score

welcome_message()

print(project_name())

efficiency_1=efficiency_score(10,11)
efficiency_2=efficiency_score(8,9)
efficiency_3=efficiency_score(4,8)

formatted_report("Asha", "Finance", efficiency_1)
formatted_report("Rahul", "IT",efficiency_2)
formatted_report("Sneha","HR", efficiency_3)

average_efficiency_score(efficiency_1,efficiency_2,efficiency_3)


# Sample Output

# Welcome to UST Employee Work Report System
# This program helps HR calculate employee performance easily.


# Current Active Project: UST Cloud Migration


# Employee:  Asha | Department:  Finance | Efficiency:  11.0  
# Needs improvement
# Employee:  Rahul | Department:  IT | Efficiency:  11.25
# Needs improvement
# Employee:  Sneha | Department:  HR | Efficiency:  20.0
# Good performance.


# Average Team Efficiency:  14.083333333333334
# Team needs improvement