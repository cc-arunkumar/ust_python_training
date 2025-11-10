# Function without arguments but with return
# Objective:
# Sometimes we need fixed information that doesn’t come from the user, like a
# default project name.
# Requirements:
# Create a function that returns the current active project name, e.g., "UST Cloud
# Migration" .
# The function should not accept any parameters.
# It should just return the value to the main program


def get_proj_name():
    return "UST cloud migration"
project=get_proj_name()
print("Current Active Project:",project)


#o/p:
#Current Active Project: UST cloud migration