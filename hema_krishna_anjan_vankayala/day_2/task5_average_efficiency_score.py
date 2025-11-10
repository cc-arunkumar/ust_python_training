#Part 5: Function with variable arguments ( args )

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

def avg_efficiency_score(*eff_scores):
    sum_of_scores = 0
    msg=""
    for score in eff_scores:
        sum_of_scores += score
    avg_scores = sum_of_scores/len(eff_scores) 

    if avg_scores>25:
        msg="Team performed above expectations."
    else:
        msg="Team needs improvement."

    return f"Average Team Efficiency: {avg_scores} \n {msg}"

#Sample Output
#avg_efficiency_score(18.75,27.5,30.0)
#'Average Team Efficiency: 25.416666666666668
# Team performed above expectations.'
