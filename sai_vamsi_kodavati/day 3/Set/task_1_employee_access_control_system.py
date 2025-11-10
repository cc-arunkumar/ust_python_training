# TASK 1 -  Employee Access Control System

prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

all_employees  = prod_access & test_access
print("Access to both servers:",all_employees)

print("Access to at least one server:",prod_access|test_access)

print("Access to only production access:",prod_access - test_access)

prod_access.add("Ravi")

test_access.discard("Rahul")

print("Final Access List:",prod_access | test_access)

# -------------------------------------------------------------------------------

# Sample Output
# Access to both servers: {'Neha', 'Amit'}
# Access to at least one server: {'Neha', 'Amit', 'Rahul', 'Priya', 'John', 'Sita'}
# Access to only production access: {'Priya', 'John'}
# Final Access List: {'Neha', 'Ravi', 'Priya', 'Amit', 'John', 'Sita'}
