#Task1
salary = [20000, 30000, 40000, 50000]
new = list(map(lambda sal : sal + (sal * 0.1), salary))
print(new)

#Task2
numbers = [101, 102, 103, 104, 105, 106]
even = list(filter(lambda x : x % 2 == 0, numbers))
print(even)

#Task3
employees = [("Rahul", 3), ("Priya", 7), ("Karan", 2), ("Divya", 6)]
sorted_employees = sorted(employees, key = lambda x : x[1])
print(sorted_employees)

#Task4
age = lambda x: "Junior" if x < 30 else ("MidLevel" if x < 45 else "Senior")
print(age(21)) 

#Task5
names = ["Arun", "Neha", "Vikram"]
dept = ["Hr", "IT", "Finance"]
combine = lambda a, b: list(map(lambda x, y: f"{x} works with {y}", names, dept))
print(combine(names, dept))