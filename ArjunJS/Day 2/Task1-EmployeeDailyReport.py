# Task: UST Employee Daily Work Report Automation
from task1_welcome import welcome_text
from task2_emp_efficiency import emp_efficiency
from task3_emp_report import emp_report
from task4_Active_Project import active_project
from task5_avg_eff_score import avg_eff_score

welcome_text()
active_project()
emp_report("Asha","Finance",emp_efficiency(10,26))
emp_report("Rahul","IT",emp_efficiency(10,20))
emp_report("Sneha","HR",emp_efficiency(10,14.3))
avg_eff_score(emp_efficiency(10,26),emp_efficiency(10,20),emp_efficiency(10,14.3))
#Output
# Welcome to UST Employee Work Report System
# This program helps HR calculate employee performance easily.
# Employee Name : Asha
# Department : Finance
# Efficiency : 26.0
# Excellent Performance
# Employee Name : Rahul
# Department : IT
# Efficiency : 20.0
# Good Performance
# Employee Name : Sneha
# Department : HR
# Efficiency : 14.3
# Need Improvement
# Average Team Efficiency : 20.1
# Team needs improvement.