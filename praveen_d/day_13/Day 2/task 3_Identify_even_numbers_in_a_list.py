# Task 3_Identify Even Numbers in a List
# You have a list of employee IDs, and you need to filter out only even IDs for an internal audit.

# Requirement:
# Use a lambda function with the filter() method to select even IDs.

# Example Input:
# ids = [101, 102, 103, 104, 105, 106]



ids = [101,102,103,104,105,106]

filtered_list= list(filter(lambda id : id%2==0, ids))

print(filtered_list)

# dentify Even Numbers in a List.py"
# [102, 104, 106]