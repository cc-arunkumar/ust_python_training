prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

print("access to both servers:" , prod_access.intersection(test_access))
print("access to at least one server:" , prod_access.union(test_access))
print("only production access:",prod_access.difference(test_access))

prod_access.add("Ravi")
test_access.discard("Rahul")

total=prod_access.union(test_access)
my_set=sorted(total)
print("Final Access List:" , my_set )

# access to both servers: {'Amit', 'Neha'}
# access to at least one server: {'Priya', 'Amit', 'Sita', 'John', 'Rahul', 'Neha'}
# only production access: {'John', 'Priya'}
# Final Access List: ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']