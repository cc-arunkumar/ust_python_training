# Part 5_ Function with variable arguments (args)
# Objective:
# After collecting data from multiple employees, HR wants to know the average
# efficiency score of the entire team.
# Requirements:
# Create a function that accepts any number of efficiency scores.
# It should calculate and print the average of all the scores.
# Based on the average:
# If average > 25 → “Team performed above expectations.”
# Otherwise → “Team needs improvement.”
# The function should only print the result and not return anything

def calculate_team_efficiency(*effiencies):
    sum=0
    for eff in effiencies:
        sum+=eff
    
    average=sum/len(effiencies)

    if average> 25:
        print("Team performed above expectations.")
    else:
        print("Team needs to improve")





