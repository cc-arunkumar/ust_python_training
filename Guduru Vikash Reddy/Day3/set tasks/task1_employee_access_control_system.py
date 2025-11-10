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
print("Access to both servers:", prod_access.intersection(test_access))
print("Access to at least one server:", prod_access.union(test_access))
print("Only production access:", prod_access.difference(test_access))
prod_access.add("Ravi")
test_access.remove("Rahul")
Finalists = prod_access.union(test_access)
print("Finalists:", sorted(Finalists))
# sample output
# Access to both servers: {'Amit', 'Neha'}
# Access to at least one server: {'Amit', 'Priya', 'Sita', 'Rahul', 'Neha', 'John'}
# Only production access: {'Priya', 'John'}
# Finalists: ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']