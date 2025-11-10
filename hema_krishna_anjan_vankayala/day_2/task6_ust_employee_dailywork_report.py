#Task1: UST Employee DailyWork Report Automation System

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

from task1_welcome_message import welcome_msg
from task4_current_projectname import current_active_project_name
from task2_efficiency_score import efficiency_score 
from task3_performance_calculator import overview_performance
from task5_average_efficiency_score import avg_efficiency_score



welcome_msg()
print(current_active_project_name())
eff_of_asha=efficiency_score(30,8)
eff_of_rahul=efficiency_score(45,10)
eff_of_sneha=efficiency_score(45,15)
overview_performance("Asha","Finance",eff_of_asha)
overview_performance("Asha","Finance",eff_of_rahul)
overview_performance("Sneha","HR",eff_of_sneha)
print(avg_efficiency_score(eff_of_sneha,eff_of_asha,eff_of_rahul))


#Sample Output
# Welcome to UST Employee Work Report System
# This program helps HR calculate employee performance easily.

# Current Active Project: UST Cloud Migration     

# Employee: Asha | Department: Finance | Efficiency: 37.5
# Excellent performance
# Employee: Asha | Department: Finance | Efficiency: 45.0
# Excellent performance
# Employee: Sneha | Department: HR | Efficiency: 30.0
# Excellent performance
# Average Team Efficiency: 37.5
# Team performed above expectations.