
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


def average_efficiency_score(*efficiency_score):
    average=sum(efficiency_score)/len(efficiency_score)
    print("Average Team Efficiency: ", average)
    if average>25:
        print("Team performed above expectations")
    else:
        print("Team needs improvement")