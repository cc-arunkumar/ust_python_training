#Task3: Function with arguments and without return

#Code
import task4_function_without_arguments_with_return
from task2_function_with_arguments_and_with_return import effi_score

def efficiency_report(name,department,efficiency_score):
    print(f"Employee: {name} | Department: {department} | Efficiency: {efficiency_score}")
    if(efficiency_score>25):
        print("Excellent Performance.")
    elif(efficiency_score>=15 and efficiency_score<=25):
        print("Good Performance.")
    else:
        print("Needs Improvement")

efficiency_report("Asha","Finance",effi_score(50,9))
efficiency_report("Rahul","IT",effi_score(30,9))
efficiency_report("Sneha","HR",effi_score(20,9))


#Sample Execution
# Welcome to UST Employee Work Report System
# This program helps HR calculate employee performance easily
# Current Active Project: UST Cloud Migration
# Employee: Asha | Department: Finance | Efficiency: 55.55555555555556
# Excellent Performance.
# Employee: Rahul | Department: IT | Efficiency: 33.333333333333336
# Excellent Performance.
# Employee: Sneha | Department: HR | Efficiency: 22.22222222222222
# Good Performance.