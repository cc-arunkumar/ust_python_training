#  Function with variable arguments ( args )
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


ids=[101,102,103,104,105,106]
even_ids=list(filter(lambda num:num%2==0,ids))
print(even_ids)


#o/p:
#[102, 104, 106]