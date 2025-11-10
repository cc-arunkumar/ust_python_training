prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}
print("Both Access: ",prod_access & test_access)
all=prod_access|test_access
print("Atleast one access: ",all)
print("Only production access: ",prod_access-test_access)
prod_access.add("Ravi")
test_access.discard("Rahul")
li=list(all)
li.sort()
print("Final access list: ",li)

# Both Access:  {'Amit', 'Neha'}
# Atleast one access:  {'Rahul', 'Neha', 'Amit', 'Priya', 'Sita', 'John'}
# Only production access:  {'Priya', 'John'}
# Final access list:  ['Amit', 'John', 'Neha', 'Priya', 'Rahul', 'Sita']
