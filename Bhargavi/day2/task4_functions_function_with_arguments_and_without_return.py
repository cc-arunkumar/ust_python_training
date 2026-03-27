#Function without arguments but with return

# Part 4: Function without arguments but with return

# Objective:
# Sometimes we need fixed information that doesn’t come from the user, like a
# default project name.

# Requirements:
# Create a function that returns the current active project name, e.g., "UST Cloud
# Migration" .
# The function should not accept any parameters.
# It should just return the value to the main program.
# Define a function that returns the current project name
def project_name():
    return "UST Cloud Migration"

# Call the function and store the result in a variable
project = project_name()

# Print the active project name
print("Current Active Project:", project)

#output
# Current Active Project: UST Cloud Migration
