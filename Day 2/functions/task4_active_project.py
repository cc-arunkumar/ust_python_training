# Part 4: Function without arguments but with return
# Objective:
# Sometimes we need fixed information that doesn’t come from the user, like a
# default project name.

def project_name():
    return "UST CloudMigration."
res = project_name()
print(res)

# sample output

# UST CloudMigration.