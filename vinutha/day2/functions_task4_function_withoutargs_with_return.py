#Function without arguments but with return

# Part 4: Function without arguments but with return
# Objective:
# Sometimes we need fixed information that doesn’t come from the user, like a
# default project name.
# Requirements:
# Create a function that returns the current active project name, e.g., "UST Cloud
# Migration" .
# The function should not accept any parameters.
# Day 2 3
# It should just return the value to the main program.

#code

# Function to get the name of the current active project
def get_active_project():
    return "UST Cloud Migration"   

# Call the function and store the result in a variable
project = get_active_project()

# Print the active project name
print("Current Active Project:", project)


#output
# PS C:\Users\303379\day2_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day2_training/task4_functions.py
# Current Active Project: UST Cloud Migration
# PS C:\Users\303379\day2_training> 

