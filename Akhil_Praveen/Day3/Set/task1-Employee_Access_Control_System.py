prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}
print("Employees who have access to both servers",prod_access.intersection(test_access))
print("Employees who have access to at least one server",prod_access.union(test_access))
print("Employees who have only production access: ",prod_access.difference(test_access))
prod_access.add("Ravi")
print("Added new employee: ",prod_access)
test_access.discard("Rahul")
print("Removed Rahul from test: ",test_access)
results = list(prod_access.union(test_access))
results.sort()
print("Final Access List: ",results)

# Employees who have access to both servers {'Neha', 'Amit'}
# Employees who have access to at least one server {'Sita', 'John', 'Priya', 'Amit', 'Rahul', 'Neha'}
# Employees who have only production access:  {'Priya', 'John'}
# Added new employee:  {'John', 'Ravi', 'Priya', 'Amit', 'Neha'}
# Removed Rahul from test:  {'Neha', 'Sita', 'Amit'}
# Final Access List:  ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']