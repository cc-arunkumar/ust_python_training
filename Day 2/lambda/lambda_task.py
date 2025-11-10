# Task 1: Calculate Bonus for Employees

salary = [10000,2000,30000,40000,50000]
res = list(map(lambda sal: sal*0.10,salary))
print(res)


# Task 2: Identify Even Numbers in a List

id = [10,20,34,45,60]
res = list(filter(lambda even :even%2==0,id))
print(res)

# Task 3: Sort Employees by Experience

employees = [("rahul",3),("madhan",1),("gowtham",5),("ramesh",4),("regan",5)]
employees.sort(key = lambda a:a[1])
print(employees)

# Task 4: Categorize Age Groups

age = int(input("Enter age:"))
category = lambda age : "Junior" if age<30 else "Mid-Level" if age <= 45 else "senior"
print(category(age))


# TASK 5 - Combine Two Lists

names=["madhan","Gowtham","dhoni"]
departments=["IT","IT","Sports"]

print(list(map(lambda name,dep : f"{name} works in {dep} department",names,departments)))

# sample output:
# [1000.0, 200.0, 3000.0, 4000.0, 5000.0]
# [10, 20, 34, 60]
# [('madhan', 1), ('rahul', 3), ('ramesh', 4), ('gowtham', 5), ('regan', 5)]
# Enter age:10
# Junior
# ['madhan works in IT department', 'Gowtham works in IT department', 'dhoni works in Sports department']




