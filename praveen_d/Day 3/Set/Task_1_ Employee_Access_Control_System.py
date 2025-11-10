# <!-- Task 1: Employee Access Control System


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