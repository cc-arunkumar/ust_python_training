#Part 4: Function without arguments but with return

# Objective:
# Sometimes we need fixed information that doesn’t come from the user, like a
# default project name.
# Requirements:
# Create a function that returns the current active project name, e.g., "UST Cloud
# Migration" .
# The function should not accept any parameters.

# It should just return the value to the main program

def current_active_project_name(name="UST Cloud Migration"):
    return f"Current Active Project: {name}\n" 

#Sample Output
#current_active_project_name()
#'Current Active Project: UST Cloud Migration'