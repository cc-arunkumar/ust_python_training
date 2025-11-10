from Task_1_greet import greet
from Task1_calculate_efficiency import calculate_employee_effiency
from Task3_report_gen import report_generator
from Day2.Task1_project_name import display_project_name
from Day2.Task1_team_efficency import calculate_team_efficiency

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