# Set Tasks
# Task 1: Employee Access Control System
# Scenario:
# Your company maintains a set of employees who have access to the Production
# Server and another set for those who have access to the Testing Server.
# Instructions:
# # Given sets
# prod_access = {"John", "Priya", "Amit", "Neha"}
# test_access = {"Amit", "Neha", "Rahul", "Sita"}
# Tasks:
# 1. Print all employees who have access to both servers.
# (Hint: intersection)
# 2. Print all employees who have access to at least one server.
# (Hint: union)
# 3. Print all employees who have only production access (not testing).
# (Hint: difference)
# 4. Add a new employee "Ravi" to production access.
# 5. Remove "Rahul" from testing access (use discard() to avoid errors if missing).
# 6. Print a final list of all employees with any type of access (sorted
# alphabetically

# Create sets of employees with access to production and test servers
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

# Find employees who have access to both servers (intersection of sets)
print("access to both servers:", prod_access.intersection(test_access))

# Find employees who have access to at least one server (union of sets)
print("access to at least one server:", prod_access.union(test_access))

# Find employees who have only production access (difference of sets)
print("only production access:", prod_access - test_access)

# Add a new employee "Ravi" to production access
prod_access.add("Ravi")

# Remove "Rahul" from test access (discard avoids error if element not present)
test_access.discard("Rahul")

# Combine both sets into a list of all employees with access
list = list(prod_access.union(test_access))

# Sort the list alphabetically
list.sort()

# Print the final organized access list
print("Final Access List:", list)


#output
# ol.py
# access to both servers: {'Amit', 'Neha'}
# access to at least one server: {'Amit', 'Neha', 'Sita', 'Priya', 'Rahul', 'John'}
# only production access: {'Priya', 'John'}
# Final Access List: ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']
# PS C:\Users\303379\day3_training>