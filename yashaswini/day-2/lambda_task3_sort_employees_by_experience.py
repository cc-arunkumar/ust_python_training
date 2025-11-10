#sort employees by experiencee
#you have a list of employees with their years of experience and you need to sort them by experience in ascending order.
#Requirement:
#use a lambda function as a sorting key


employees = [("ramesh", 3),("suresh", 7),("seeta", 2),("geeta", 5)]
sorted_emp=sorted(employees,key=lambda x:x[1])
print(sorted_emp)


#o/p:
#[('seeta', 2), ('ramesh', 3), ('geeta', 5), ('suresh', 7)]