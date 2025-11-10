prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

print("Employees who have access to both servers: ",prod_access & test_access)
print("Employees who have access to at least one server: ",prod_access | test_access)
print("Employees who have only production access: ",prod_access - test_access)

prod_access.add("Ravi")
test_access.discard("Rahul")

final_list = list(prod_access | test_access)
final_list.sort()
print("Final list: ",final_list)

# output

# Employees who have access to both servers:  {'Amit', 'Neha'}
# Employees who have access to at least one server:  {'Amit', 'Sita', 'Rahul', 'Priya', 'John', 'Neha'}
# Employees who have only production access:  {'Priya', 'John'}
# Final list:  ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']