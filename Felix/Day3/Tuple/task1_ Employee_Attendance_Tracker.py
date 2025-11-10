attendance = (
 ("E101", "John", 5),
 ("E102", "Priya", 3),
 ("E103", "Amit", 4),
 ("E104", "Neha", 2)
)
print("Employee attended more tha 3 days:")
count = 0
max = 0
name1 = attendance[1]
for (emp_id,name,days) in attendance:
    if  days >= 4:
        print(name)
    else:
        count += 1
    if days > max:
        max=days
        name1 = name

print("Number of employees present less than 4 days: ",count)
print(f"Employee with highest attendance: {name1} ({max})")


# output

# Employee attended more tha 3 days:
# John
# Amit
# Number of employees present less than 4 days:  2
# Employee with highest attendance: John (5)