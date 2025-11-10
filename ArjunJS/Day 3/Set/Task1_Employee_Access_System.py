#Task 1: Employee Access Control System
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}
print(f"Both Access : {prod_access & test_access}")
print(f"Atlest one : {prod_access | test_access}")
print(f"Only Production : {prod_access - test_access}")
test_access.discard("Rahul")
new = prod_access | test_access
new_list=list(new)
new_list.sort()
print(new_list)
#Output
# Both Access : {'Neha', 'Amit'}
# Atlest one : {'John', 'Amit', 'Sita', 'Priya', 'Neha', 'Rahul'}
# Only Production : {'John', 'Priya'}
# ['Amit', 'John', 'Neha', 'Priya', 'Sita']