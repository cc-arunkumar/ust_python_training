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

def marks(*args):
    total1=sum(args)
    percentage=(total1/len(args)*100)*100
    print("percentage",percentage)
    if (percentage>25):
        print(" Team performed above expectations")
    else:
        print("Team needs improvement")

marks(100,90,70,88)

# sample output
#  percentage 870000.0
#  Team performed above expectations