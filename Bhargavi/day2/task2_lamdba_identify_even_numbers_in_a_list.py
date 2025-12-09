#Identify Even Numbers in a List

# Task 2: Identify Even Numbers in a List

# You have a list of employee IDs, and you need to filter out only even IDs for an internal audit.

# Requirement:
# Use a lambda function with the filter() method to select even IDs.

# Example Input:
# ids = [101, 102, 103, 104, 105, 106]

# Expected Output:
# [102, 104, 106]

# (Hint: Use filter(lambda x: condition, list))


# List of employee IDs
ids = [101, 102, 103, 104, 105, 106]

# Use filter with a lambda function to select only even IDs
# Lambda checks if ID is divisible by 2 (x % 2 == 0)
even_ids = list(filter(lambda x: x % 2 == 0, ids))

# Print the list of even IDs
print(even_ids)


# Output:
# [102, 104, 106]


