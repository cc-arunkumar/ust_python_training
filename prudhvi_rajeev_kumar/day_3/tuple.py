# tuple1 = (1, 2, 3, 3, 4, 5, 3, 4, 5)
# list1 = []
# for i in range(len(tuple1)):
#     list1.append(tuple1[i] * 3)
# tuple2 = tuple(list1)
# print(tuple2)

# for i in range(len(tuple1)):
#     if tuple1[i] == 4 and 5:
#         print(True)

# print(1 in tuple1)
# print(tuple1.index(3))
# print(tuple1.count(3))


# data = (name, age, salary) = ('Alice', 30, 70000)

# for (name, age, salary) in [data]:
#     print(f"Name: {name}, Age: {age}, Salary: {salary}")

attendance = (
 ("E101", "John", 5),
 ("E102", "Priya", 3),
 ("E103", "Amit", 4),
 ("E104", "Neha", 2)
)

for employee_id, employee_name, days_present in attendance:
    if days_present > 3:
        print(f"Name : {employee_name}")

# for employee_id, employee_name, days_present in attendance:
#     counti = 0
#     if days_present < 4:
#         count = counti + 1
#         print(counti)


max_attendance = attendance[0]
for days_present in attendance:
    if days_present[2] > max_attendance[2]:
        max_attendance = days_present
        print(max_attendance)


