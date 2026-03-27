#Employee Access Control System

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

# Initial sets of users with production and test access
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

# Find users who have both production and test access
both_access = prod_access.intersection(test_access)
print("Both Access:", both_access)

# Find users who have at least one type of access (union of sets)
at_least_one = prod_access.union(test_access)
print("At Least One Access:", at_least_one)

# Find users who have only production access (not in test)
only_prod = prod_access.difference(test_access)
print("Only Production Access:", only_prod)

# Add a new user to production access
prod_access.add("Ravi")

# Remove a user from test access
test_access.discard("Rahul")

# Create final sorted list of all users with any access
final_access = sorted(prod_access.union(test_access))
print("Final Access List:", final_access)


# Output:
# Both Access: {'Amit', 'Neha'}
# At Least One Access: {'John', 'Neha', 'Amit', 'Sita', 'Priya', 'Rahul'}
# Only Production Access: {'Priya', 'John'}
# Final Access List: ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']
