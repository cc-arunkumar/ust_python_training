prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

print(prod_access.intersection(test_access))
print(prod_access.union(test_access))
print(prod_access.difference(test_access))
prod_access.add("Ravi")
print(prod_access)
test_access.discard("Rahul")
print(test_access)
print(prod_access.union(test_access))
sorted_set = set(sorted(prod_access.union(test_access)))
print(sorted_set)









