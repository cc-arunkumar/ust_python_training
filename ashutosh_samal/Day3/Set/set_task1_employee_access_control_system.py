#Task 1: Employee Access Control System

# Sets representing employees with access to different servers
prod_access = {"John", "Priya", "Amit", "Neha"}  # Employees with production server access
test_access = {"Amit", "Neha", "Rahul", "Sita"}  # Employees with testing server access

# Printing employees who have access to both servers (intersection of the two sets)
print("Employee who have access to both servers:", prod_access.intersection(test_access))

# Printing employees who have access to at least one server (union of the two sets)
print("Employee who have access to at least one server:", prod_access.union(test_access))

# Printing employees who have only production server access (difference between prod_access and test_access)
print("Employee who have only production access:", prod_access.difference(test_access))

# Adding a new employee "Ravi" to production access set
prod_access.add("Ravi")

# Removing "Rahul" from the test access set (discard method doesn't raise an error if the element doesn't exist)
test_access.discard("Rahul")

# Combining both sets and converting to a sorted list
final_access = list(prod_access.union(test_access))  # Union of prod_access and test_access
final_access.sort()  # Sorting the list in ascending order

# Printing the final sorted list of employees with access to at least one server
print("Final Access List:", final_access)



#Sample Execution
# Employee who have access to both servers: {'Amit', 'Neha'}
# Employee who have access to atleast one server: {'John', 'Rahul', 'Sita', 'Neha', 'Amit', 'Priya'}
# Employee who have only production access: {'John', 'Priya'}
# Final Access List: ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']