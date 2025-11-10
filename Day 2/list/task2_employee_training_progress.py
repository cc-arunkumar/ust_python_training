# Task 2: Employee Training Progress
# Tracker
# Scenario:
# You are tracking the employees who have completed their mandatory “Cyber
# Security Awareness” training.


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

# {'Neha', 'Amit'}
# {'Sita', 'Priya', 'Neha', 'Rahul', 'Amit', 'John'}
# {'John', 'Priya'}
# {'Priya', 'Neha', 'Rahul', 'Amit', 'John'}    
# {'Amit', 'Neha', 'Sita'}
# ['Amit', 'John', 'Neha', 'Priya', 'Rahul', 'Sita']
# Both Access:['Amit', 'Neha']



