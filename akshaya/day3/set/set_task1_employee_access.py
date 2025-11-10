# Given sets employee access
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

both_access = prod_access.intersection(test_access)
print("Both Access:", both_access)

at_least_one = prod_access.union(test_access)
print("At Least One Access:", at_least_one)

only_production = prod_access.difference(test_access)
print("Only Production Access:", only_production)

prod_access.add("Ravi")

test_access.discard("Rahul")

final_access_list = sorted(prod_access.union(test_access))
print("Final Access List:", final_access_list)



#sample output
# PS C:\Users\303375\Downloads\Tasks> python set_task1_employee_access.py
# Both Access: {'Neha', 'Amit'}
# At Least One Access: {'Sita', 'Priya', 'John', 'Amit', 'Rahul', 'Neha'}
# Only Production Access: {'John', 'Priya'}
# Final Access List: ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']
