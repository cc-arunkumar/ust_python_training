#Task 1: Employee Access Control System

prod_access={"John","Priya","Amit","Neha"}
test_access={"Amit","Neha","Rahul","Sita"}

both_access=prod_access.intersection(test_access)
print(f"Both Access:{both_access}")

one_access=prod_access.union(test_access)
print(f"Atleast one Access:{one_access} ")

only_production_access=prod_access.difference(test_access)
print(f"Only production Access:{only_production_access}")

prod_access.add("Ravi")
test_access.discard("Rahul")

final_list=sorted(prod_access.union(test_access))
print(f"Final Access List:{final_list}")