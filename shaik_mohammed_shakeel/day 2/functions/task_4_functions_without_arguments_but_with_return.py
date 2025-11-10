
# Task 4: Function without arguments but with return

# Objective:
# Sometimes we need fixed information that doesn’t come from the user, like a
# default project name.

# Requirements:
# Create a function that returns the current active project name, e.g., "UST Cloud
# Migration" .
# The function should not accept any parameters.
# Day 2 3
# It should just return the value to the main program.

def curr_act_proj():
    return "UST Cloud Migration"
project=curr_act_proj()
print("Current Active Project is : ",project)

#Sample Output
# Current Active Project is :  UST Cloud Migration