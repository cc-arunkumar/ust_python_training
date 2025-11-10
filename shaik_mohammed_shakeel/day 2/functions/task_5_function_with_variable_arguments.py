
# Part 5: Function with variable arguments ( args )

# Objective:
# After collecting data from multiple employees, HR wants to know the average
# efficiency score of the entire team.

# Requirements:
# Create a function that accepts any number of efficiency scores.
# It should calculate and print the average of all the scores.
# Based on the average:
# If average > 25 → “Team performed above expectations.”
# Otherwise → “Team needs improvement.”
# The function should only print the result and not return anything.


def avg_eff_score(*efficiency_score):
    total = 0
    count = 0
    for i in efficiency_score:
        total += i
        count += 1
    print("Average Team Efficiency: ",total/count)
    if((total//count)>25):
        print("Team performed above expectations.")
    else:
        print("Team needs improvement.")
    
avg_eff_score(20.32,10,13,7)

#sample Output
# Average Team Efficiency:  12.58
# Team needs improvement.