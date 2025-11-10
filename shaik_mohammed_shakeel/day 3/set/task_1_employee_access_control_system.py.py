# Task 1- Employee Access Control System

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
print("Both Access: ",prod_access.intersection(test_access))
print("Atleast One Access: ",prod_access.union(test_access))
print("Only Production Access: ",prod_access - test_access)
prod_access.add("Ravi")
print("Prod Access after adding Ravi: ",prod_access)
test_access.discard("Rahul")
print("Test Access after discarding Rahul: ",test_access)
combined=prod_access.union(test_access)
combined_sorted=sorted(combined)
print("Final List: ",combined_sorted)

#sample Output
# Both Access:  {'Amit', 'Neha'}
# Atleast One Access:  {'Amit', 'John', 'Rahul', 'Priya', 'Sita', 'Neha'}
# Only Production Access:  {'Priya', 'John'}
# Prod Access after adding Ravi:  {'Amit', 'Ravi', 'John', 'Priya', 'Neha'}
# Test Access after discarding Rahul:  {'Amit', 'Sita', 'Neha'}
# Final List:  ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']