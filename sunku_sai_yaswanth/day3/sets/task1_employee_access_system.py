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
# Task 1: Employee Access Control System
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}


print("Acess to both servers:",prod_access.intersection(test_access))


print("access to at least one server:",prod_access.union(test_access))

print("only production acess:",prod_access.difference(test_access))

prod_access.add("Ravi")
print("added ravi:",prod_access)

test_access.remove("Rahul")
print(test_access)

cunio_of_both=prod_access.union(test_access)
sort=sorted(cunio_of_both)


# sample output
# Acess to both servers: {'Amit', 'Neha'}
# access to at least one server: {'John', 'Sita', 'Neha', 'Amit', 'Priya', 'Rahul'}
# only production acess: {'John', 'Priya'}
# added ravi: {'John', 'Ravi', 'Neha', 'Amit', 'Priya'}
# {'Amit', 'Sita', 'Neha'}