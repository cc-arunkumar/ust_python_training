#Task 1: Employee Access Control System
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

print("Both Access: ",prod_access&test_access)
print("At Least One Access: ",prod_access|test_access)
print("Only Production Access: ",prod_access-test_access)
print("Final Access List: ",list(prod_access|test_access))

# #Sample output
# Both Access:  {'Neha', 'Amit'}
# At Least One Access:  {'Neha', 'Sita', 'John', 'Priya', 'Rahul', 'Amit'}
# Only Production Access:  {'John', 'Priya'}
# Final Access List:  ['Neha', 'Sita', 'John', 'Priya', 'Rahul', 'Amit']