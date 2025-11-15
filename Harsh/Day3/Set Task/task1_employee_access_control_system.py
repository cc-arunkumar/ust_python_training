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

# Print employees with access to both servers
print("access to both servers:" , prod_access.intersection(test_access))

# Print employees with access to at least one server
print("access to at least one server:" , prod_access.union(test_access))

# Print employees with only production access
print("only production access:",prod_access.difference(test_access))

# Add Ravi to production access
prod_access.add("Ravi")

# Remove Rahul from testing access
test_access.discard("Rahul")

# Print final sorted list of all employees with any access
total=prod_access.union(test_access)
my_set=sorted(total)
print("Final Access List:" , my_set )

# access to both servers: {'Amit', 'Neha'}
# access to at least one server: {'Priya', 'Amit', 'Sita', 'John', 'Rahul', 'Neha'}
# only production access: {'John', 'Priya'}
# Final Access List: ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']