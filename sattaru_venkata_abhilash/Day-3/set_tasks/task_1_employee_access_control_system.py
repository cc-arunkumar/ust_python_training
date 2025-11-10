# Task 1: Employee Access Control System
# Scenario:
# Your company maintains a set of employees with access to Production and Testing servers.

# Given sets
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

# 1. Employees who have access to both servers
print("Both Access:", prod_access & test_access)

# 2. Employees who have access to at least one server
print("At Least One Access:", prod_access | test_access)

# 3. Employees who have only production access (not testing)
print("Only Production Access:", prod_access - test_access)

# 4. Add a new employee "Ravi" to production access
prod_access.add("Ravi")

# 5. Remove "Rahul" from testing access
test_access.discard("Rahul")

# 6. Final list of all employees with any type of access (sorted alphabetically)
all_access = prod_access | test_access
print("Final Access List:", sorted(all_access))


# Sample Output:
# Both Access: {'Amit', 'Neha'}
# At Least One Access: {'John', 'Priya', 'Amit', 'Neha', 'Rahul', 'Sita'}
# Only Production Access: {'John', 'Priya'}
# Final Access List: ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']
