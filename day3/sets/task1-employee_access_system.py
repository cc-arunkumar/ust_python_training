# Task 1: Employee Access Control System
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

#  Print all employees who have access to both server
print("Acess to both servers:",prod_access.intersection(test_access))
# Print all employees who have access to at least one server.

print("access to at least one server:",prod_access.union(test_access))
# Print all employees who have only production access (not testing).
print("only production acess:",prod_access.difference(test_access))
#  Add a new employee "Ravi" to production access.
prod_access.add("Ravi")
print("added ravi:",prod_access)
#  Remove "Rahul" from testing access
test_access.remove("Rahul")
print(test_access)
#  Print a final list of all employees with any type of access (sorted
# alphabetically).
cunio_of_both=prod_access.union(test_access)
sort=sorted(cunio_of_both)


# sample output
# Acess to both servers: {'Amit', 'Neha'}
# access to at least one server: {'John', 'Sita', 'Neha', 'Amit', 'Priya', 'Rahul'}
# only production acess: {'John', 'Priya'}
# added ravi: {'John', 'Ravi', 'Neha', 'Amit', 'Priya'}
# {'Amit', 'Sita', 'Neha'}