#Employee Access Control System

prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

both_access = prod_access.intersection(test_access)
print("Both Access:", both_access)

at_least_one = prod_access.union(test_access)
print("At Least One Access:", at_least_one)

only_prod = prod_access.difference(test_access)
print("Only Production Access:", only_prod)

prod_access.add("Ravi")

test_access.discard("Rahul")

final_access = sorted(prod_access.union(test_access))
print("Final Access List:", final_access)

# Both Access: {'Amit', 'Neha'}
# At Least One Access: {'John', 'Neha', 'Amit', 'Sita', 'Priya', 'Rahul'}
# Only Production Access: {'Priya', 'John'}
# Final Access List: ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']