completed=["john","priya","amit"]
completed.append("neha")
completed.append("rahul")
print(completed)
completed.remove("amit")
print(completed)

pending=["meena","vivek","sita"]
# completed.extend(pending)
# all_employee=[completed]
all_employee=completed+pending
print(all_employee)
all_employee.sort()
print(all_employee)
print(f"\ntotal no. of employees:{len(all_employee)}")