# Task 2: Identify Even Numbers in a List

# You have a list of employee IDs, and you need to filter out only even IDs for an internal audit.

# Requirement:
# Use a lambda function with the filter() method to select even IDs.


ids = [101, 102, 103, 104, 105, 106]
even_no=list(filter(lambda x: x%2==0, ids))
print(even_no)
# sample output
# [102, 104, 106]

