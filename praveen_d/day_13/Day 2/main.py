# Task: UST Employee DailyWork Report
# Automation
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


from task_1_part_1_greet import greet
from task1_part_2_calculate_efficiency import calculate_employee_effiency
from task1_part_3_report_gen import report_generator
from task1_part_4_project_name import display_project_name
from task1_part_5_team_efficency import calculate_team_efficiency

# Part:1
greet()

# part 2:
hours_worked=int(input("Enter the hours you have worked:"))
tasks_completed=int(input("Enter the number of tasks you complete:"))
employee_effiency_score= calculate_employee_effiency(hours_worked,tasks_completed)
print(employee_effiency_score)

# part3:
report=report_generator("Praveen", "full_stack",employee_effiency_score)

# part 4:
current_project_name=display_project_name()
print(f"The current project name is:{current_project_name}")

# part 5:
calculate_team_efficiency(20,25,30)


# PS C:\UST python> & C:/Users/303489/AppData/Local/Programs/Python/Python312/python.exe "c:/UST python/Day2/main.py"

# Welcome to UST Employee Work Report System
# Enter the hours you have worked:20
# Enter the number of tasks you complete:40
# 20.0
# Employee name:Praveen
# Employee department:full_stack
# Employee Efficiency score:20.0
# Good perfomance
# The current project name is:Migration
# Team needs to improve
# PS C:\UST python> 