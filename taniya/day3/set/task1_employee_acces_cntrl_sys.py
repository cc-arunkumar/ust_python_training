# Define two sets of employees with access
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

# Intersection → common elements in both sets
print(prod_access.intersection(test_access))

# Union → all unique elements from both sets
print(prod_access.union(test_access))

# Difference → elements in prod_access but not in test_access
print(prod_access.difference(test_access))

# Add a new element to prod_access
prod_access.add("Ravi")
print(prod_access)

# Remove an element from test_access
test_access.remove("Rahul")
print(test_access)

# Union again after modifications
final_list = prod_access.union(test_access)

# Print sorted list of all unique names
print(sorted(final_list))
# print(final_list)  # (unsorted version if needed)

# -------------------------
# Expected Output:
# {'Neha', 'Amit'}
# {'Rahul', 'John', 'Priya', 'Neha', 'Sita', 'Amit'}
# {'John', 'Priya'}
# {'John', 'Priya', 'Neha', 'Amit', 'Ravi'}
# {'Sita', 'Neha', 'Amit'}
# ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']