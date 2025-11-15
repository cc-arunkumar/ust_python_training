# Employee Access Control System
# Your company maintains a set of employees who have access to the Production
# Server and another set for those who have access to the Testing Server.

# Sets representing users with production and test access
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

# Print users who have both production and test access (intersection)
print("Both Access: ", prod_access & test_access)

# Get all users who have at least one access (union)
all = prod_access | test_access
print("Atleast one access: ", all)

# Print users who have only production access (difference)
print("Only production access: ", prod_access - test_access)

# Add a new user to production access and remove a user from test access
prod_access.add("Ravi")       # Add "Ravi" to production access
test_access.discard("Rahul")  # Remove "Rahul" from test access, if present

# Convert the union of all users to a sorted list and print it
li = list(all)
li.sort()
print("Final access list: ", li)


#Sample output

# Both Access:  {'Amit', 'Neha'}
# Atleast one access:  {'Rahul', 'Neha', 'Amit', 'Priya', 'Sita', 'John'}
# Only production access:  {'Priya', 'John'}
# Final access list:  ['Amit', 'John', 'Neha', 'Priya', 'Rahul', 'Sita']
