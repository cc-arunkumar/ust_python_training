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
# alphabetically).

prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

# 1. Print all employees who have access to both servers.
print("Both Access:",prod_access&test_access)

# 2. Print all employees who have access to at least one server.
print("At Least One Access:",prod_access | test_access)

# 3. Print all employees who have only production access (not testing).
print("Only Production Access:",prod_access-test_access)

# 4. Add a new employee "Ravi" to production access.
prod_access.add("Ravi")

# 5. Remove "Rahul" from testing access (use discard() to avoid errors if missing).
test_access.discard("Rahul")
final_list=prod_access.union(test_access)

# 6. Print a final list of all employees with any type of access (sortedalphabetically).
print("Final Access List:",sorted(final_list))

# Sample Output

# Both Access: {'Neha', 'Amit'}

# At Least One Access: {'Sita', 'John', 'Priya', 'Amit', 'Neha', 'Rahul'}

# Only Production Access: {'John', 'Priya'}

# Final Access List: ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']