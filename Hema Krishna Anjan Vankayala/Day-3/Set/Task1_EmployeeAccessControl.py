#Task 1: Employee Access Control System
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

print("Both Access:", prod_access.intersection(test_access))
print("At Least One Access:",prod_access.union(test_access))
print("Only Production Access:",prod_access.difference(test_access))
prod_access.add("Ravi")
test_access.discard("Rahul")
all_acess = prod_access.union(test_access)
print("Final Access",sorted(list(all_acess)))

#Sample Output
# Both Access: {'Neha', 'Amit'}
# At Least One Access: {'John', 'Neha', 'Amit', 'Rahul', 'Sita', 'Priya'}
# Only Production Access: {'Priya', 'John'}
# Final Access ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']