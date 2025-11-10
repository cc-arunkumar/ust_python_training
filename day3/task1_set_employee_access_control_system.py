#employee access control system

prod_access={"john","priya","amit","neha"}
test_access={"amit","neha","rahul","sita"}
print("employees have access to both servers: ",prod_access & test_access)
print("employees have access to atleast one server ",prod_access|test_access)
print("employees who have only production access",prod_access-test_access)
prod_access.add("ravi")
print("updated production access list",prod_access)
test_access.remove("rahul")
print("updated test access list",test_access)
all_employees = sorted(prod_access | test_access)
print("sorted list",all_employees)

#sample output
# employees have access to both servers:  {'amit', 'neha'}
# employees have access to atleast one server  {'neha', 'sita', 'priya', 'john', 'amit', 'rahul'}
# employees who have only production access {'john', 'priya'}
# updated production access list {'neha', 'priya', 'john', 'amit', 'ravi'}
# updated test access list {'neha', 'amit', 'sita'}
# sorted list ['amit', 'john', 'neha', 'priya', 'ravi', 'sita']