# Task 2: Identify Even Numbers in a List
# Requirement:
# You have a list of employee IDs and need to filter out only even IDs for an internal audit.
# Use a lambda function with the filter() method to select even IDs.

ids = [101, 102, 103, 104, 105, 106]
Even = list(filter(lambda x: x % 2 == 0, ids))
print(Even)

# Sample Output:
# [102, 104, 106]
