prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

#  Print all employees who have access to both servers.
print("Both access",prod_access & test_access)
# Print all employees who have access to at least one server.
print("At Least One Access:",prod_access | test_access)
# Print all employees who have only production access (not testing).
print("At Least One Access: ",prod_access-test_access)
#adding new employee
prod_access.add("Ravi")
#Removing Rahul from test_access
test_access.discard("Rahul")
#finallist of all in sorted
finalist=list(prod_access | test_access)
finalist.sort()
print("Final Access List:",finalist)


# ======sample Execution========
# Both access {'Amit', 'Neha'}
# At Least One Access: {'John', 'Sita', 'Priya', 'Rahul', 'Neha', 'Amit'}
# At Least One Access:  {'John', 'Priya'}
# Final Access List: ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']