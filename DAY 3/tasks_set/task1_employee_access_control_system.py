"""
Task 1: Employee Access Control System
Scenario:
Your company maintains a set of employees who have access to the Production
Server and another set for those who have access to the Testing Server.


"""

prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

# HAVING BOTH ACCESS
both_access=prod_access.intersection(test_access)
print(both_access)

# ATLEAST ONE ACCESS
atleast_1_access=prod_access.union(test_access)
print(atleast_1_access)

#ONE ACCESS ONLY
one_access=prod_access.difference(test_access)
print(one_access)

# ADD EMPLOYEES
prod_access.add("Ravi")
print(prod_access)

#REMOVING
test_access.remove("Rahul")
print(test_access)

#SORTING
sample_union=prod_access.union(test_access)
sorted_prod_access=sorted(sample_union)

# sorted_test_access=sorted(test_access)

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