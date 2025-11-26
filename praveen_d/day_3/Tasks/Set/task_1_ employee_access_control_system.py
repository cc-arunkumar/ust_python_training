# <!-- Task 1: Employee Access Control System
# Scenario:
# Your company maintains a set of employees who have access to the Production
# Server and another set for those who have access to the Testing Server.
# Instructions:
# # Given sets
# prod_access = {"John", "Priya", "Amit", "Neha"}
# test_access = {"Amit", "Neha", "Rahul", "Sita"}
# Tasks:
# 1. Print all employees who have access to both servers.
# (Hint: intersection)
# 2. Print all employees who have access to at least one server.
# (Hint: union)
# 3. Print all employees who have only production access (not testing).
# (Hint: difference)
# 4. Add a new employee "Ravi" to production access.
# 5. Remove "Rahul" from testing access (use discard() to avoid errors if missing).
# 6. Print a final list of all employees with any type of access (sorted
# alphabetically).
# Expected Output(sample):
# Set Tasks 1
# Both Access: {'Amit', 'Neha'}
# At Least One Access: {'John', 'Priya', 'Amit', 'Neha', 'Rahul', 'Sita'}
# Only Production Access: {'John', 'Priya'}
# Final Access List: ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']

prod_acess={"John","Priya","Amit","Neha"}
test_acess={"Amit","Neha","Rahul","Sita"}

print(prod_acess& test_acess)#both so intersection

print(prod_acess|test_acess)#atleast one so union

print(prod_acess-test_acess)

prod_acess.add("Ravi")

test_acess.discard("Rahul")

all_acess=prod_acess | test_acess
sorted_List=list(all_acess)
sorted_List.sort()

print(sorted_List)

#EXPECTED OUTPUT:
# {'Neha', 'Amit'}
# {'Neha', 'Rahul', 'Priya', 'Amit', 'Sita', 'John'}
# {'Priya', 'John'}
# ['Amit', 'John', 'Neha', 'Priya', 'Ravi', 'Sita']