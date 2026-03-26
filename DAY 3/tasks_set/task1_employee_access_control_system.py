"""
Task 1: Employee Access Control System
Scenario:
Your company maintains a set of employees who have access to the Production
Server and another set for those who have access to the Testing Server.

"""

# Sets storing employees with access to Production and Testing servers
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

# Employees having both Production and Testing access
both_access=prod_access.intersection(test_access)
print(both_access)

# Employees having at least one type of access
atleast_1_access=prod_access.union(test_access)
print(atleast_1_access)

# Employees with Production access only
one_access=prod_access.difference(test_access)
print(one_access)

# Add an employee to Production access
prod_access.add("Ravi")
print(prod_access)

# Remove an employee from Testing access
test_access.remove("Rahul")
print(test_access)

# Combine both sets and sort the employees
sample_union=prod_access.union(test_access)
sorted_prod_access=sorted(sample_union)

#print sorted union
print(sorted_prod_access)


""" 
SAMPLE OUTPUT

{'Amit', 'Neha'}
{'Sita', 'Rahul', 'Amit', 'John', 'Priya', 'Neha'}
{'John', 'Priya'}
{'Amit', 'John', 'Priya', 'Neha', 'Ravi'}
{'Amit', 'Sita', 'Neha'}
['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']

"""
