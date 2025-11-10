#Task 1: Employee Access Control System

prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

print("Employee who have access to both servers:",prod_access.intersection(test_access))
print("Employee who have access to atleast one server:",prod_access.union(test_access))
print("Employee who have only production access:",prod_access.difference(test_access))

prod_access.add("Ravi")
test_access.discard("Rahul")
final_access=list(prod_access.union(test_access))
final_access.sort()
print("Final Access List:",final_access)


#Sample Execution
# Employee who have access to both servers: {'Amit', 'Neha'}
# Employee who have access to atleast one server: {'John', 'Rahul', 'Sita', 'Neha', 'Amit', 'Priya'}
# Employee who have only production access: {'John', 'Priya'}
# Final Access List: ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']