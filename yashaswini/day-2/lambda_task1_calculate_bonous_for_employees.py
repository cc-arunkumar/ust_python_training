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


sal=int(input("Enter the salary:"))
bonous_salary=lambda sal:sal+(sal*0.10)
print("bonous=",bonous_salary(sal))


#o/p:
#Enter the salary:55000
#bonous= 60500.0