# Employee Access Control System


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
both_access=prod_access.intersection(test_access)
print("both access:",both_access)
atleast_one_access=prod_access.union(test_access)
print("atleast one access:",atleast_one_access)
only_prod_access=prod_access.difference(test_access)
print("only production access:",only_prod_access)
prod_access.add("Ravi")
test_access.discard("Rahul")
final_access_list=sorted(prod_access.union(test_access))
print("Final access list:",final_access_list)

#o/p:
# both access: {'Amit', 'Neha'}
# atleast one access: {'Priya', 'Neha', 'Rahul', 'Amit', 'John', 'Sita'}
# only production access: {'Priya', 'John'}
# Final access list: ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']