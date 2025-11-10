#Task5: Function with variable arguments

from task3_Function_with_arguments_and_without_return import effi_score
def avg_efficiency(*scores):
    avg = sum(scores) / len(scores)
    print(f"Average Team Efficiency: {avg:.2f}")
    if avg > 25:
        print("Team performed above expectations")
    else:
        print("Team needs improvement")


avg_efficiency(
    effi_score(50, 9),
    effi_score(30, 9),
    effi_score(20, 9)
)

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
# Average Team Efficiency: 37.04
# Team performed above expectations

