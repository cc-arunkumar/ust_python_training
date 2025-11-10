# Task 1: Employee Access Control System
# Scenario:
# Your company maintains a set of employees who have access to the Production
# Server and another set for those who have access to the Testing Server.


prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

# HAVING BOTH ACCESS
common = prod_access.intersection(test_access)
print(common)

# ATLEAST ONE ACCESS
at_least_one = prod_access.union(test_access)
print(at_least_one)

#ONE ACCESS ONLY
only_one = prod_access.difference(test_access)
print(only_one)

# ADD EMPLOYEES
prod_access.add("Rahul")
print(prod_access)

#REMOVING
test_access.remove("Rahul")
print(test_access)


#SORTING
all_employess = prod_access.union(test_access)
sorted_list = sorted(all_employess)
print(sorted_list)

common = prod_access.intersection(test_access)
sort_common = sorted(common)
print(f"Both Access:{sort_common}")

# sample output:

# {'Amit', 'Neha'}
# {'Rahul', 'Sita', 'Priya', 'Amit', 'John', 'Neha'}
# {'Priya', 'John'}
# {'Rahul', 'Priya', 'Amit', 'John', 'Neha'}    
# {'Amit', 'Neha', 'Sita'}
# ['Amit', 'John', 'Neha', 'Priya', 'Rahul', 'Sita']
# Both Access:['Amit', 'Neha']



