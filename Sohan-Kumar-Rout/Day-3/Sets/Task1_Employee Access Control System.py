#Task 1: Employee Access Control System


#Code 
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

iteration_set = prod_access & test_access
union_set = prod_access | test_access
production_set = prod_access - test_access

prod_access.add("Ravi")
test_access.discard("Rahul")
sorted_list=sorted(prod_access)
print("Both Access : ",iteration_set)
print("At least one Access : ",union_set)
print("Only Production Access :",production_set)
print("Final Access List",sorted_list)

#Output
# Both Access :  {'Neha', 'Amit'}
# At least one Access :  {'Rahul', 'John', 'Amit', 'Sita', 'Neha', 'Priya'}
# Only Production Access : {'Priya', 'John'}
# Final Access List ['Amit', 'John', 'Neha', 'Priya', 'Ravi']
