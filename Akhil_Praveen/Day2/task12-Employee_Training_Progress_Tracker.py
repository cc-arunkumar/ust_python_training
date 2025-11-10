completed = ["John", "Priya", "Amit"]
completed.append("Neha")
completed.append("Rahul")
completed.remove("Amit")
pending = ["Meena", "Vivek", "Sita"]
all_employees = completed+pending
all_employees.sort()
print(all_employees)
print(len(all_employees))

# ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# 7