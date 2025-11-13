#Task1 Employee Access Control System
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}
print("Both Access: ",prod_access & test_access)
print("At Least One Access: ",prod_access|test_access)
print("Only Production Access: ",prod_access-test_access)
prod_access.add("Ravi")
test_access.discard("Rahul")
list2=list(prod_access|test_access)
print("Final Access List: ",sorted(list2))

#Sample Execution
# Both Access:  {'Neha', 'Amit'}
# At Least One Access:  {'Neha', 'John', 'Rahul', 'Sita', 'Priya', 'Amit'}
# Only Production Access:  {'Priya', 'John'}
# Final Access List:  ['Amit', 'John', 'Neha', 'Priya', 'Sita']