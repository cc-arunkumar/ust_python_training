# Part 5: Function with variable arguments (*args)
# Objective:
# Accept any number of efficiency scores, calculate their average,
# and print the team performance result.
# The function does not return any value.

def average_efficiency_score(*efficiency_score):
    average = sum(efficiency_score) / len(efficiency_score)
    print(f"Average Team Efficiency: {average:.1f}")
    
    if average > 25:
        print("Team performed above expectations.")
    else:
        print("Team needs improvement.")


# Sample Output:
# >>> average_efficiency_score(26.0, 20.0, 14.3)
# Average Team Efficiency: 20.1
# Team needs improvement.
