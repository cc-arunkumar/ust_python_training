from functools import reduce

employees = {
    "Alice": 70000,
    "Bob": 50000,
    "Charlie": 60000,
    "Diana": 80000
}
sorted_employees = dict(sorted(employees.items(), key=lambda item: item[1]))
print(sorted_employees)

overtime_status = lambda hours : "overtime" if hours > 8 else "regular"
print(overtime_status(9))

salaries = [40000, 50000, 60000, 70000, 80000]
bonus = list(map(lambda sal : sal * 0.05, salaries))
print(bonus)

new = list(filter(lambda sal : sal > 70000, salaries))
print(new)

value = [1,2,3,4,5,6]
solution = reduce(lambda a,b : a + b, value )
print(solution)

