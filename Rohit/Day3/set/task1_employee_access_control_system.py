prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}
print(prod_access.intersection(test_access))
print(prod_access.union(test_access))
print(prod_access.difference(test_access))
prod_access.add("Ravi")
test_access.discard("Rahul")
finalList = set(sorted(prod_access.union(test_access)))
print(finalList)

# ===============sample output===================
# {'Amit', 'Neha'}
# {'Priya', 'Neha', 'Rahul', 'John', 'Sita', 'Amit'}
# {'John', 'Priya'}
# {'Priya', 'Neha', 'John', 'Sita', 'Amit', 'Ravi'}