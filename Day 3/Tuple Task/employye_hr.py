# Sample data
attendance = (
    ("E101", "John", 5),
    ("E102", "Priya", 3),
    ("E103", "Amit", 4),
    ("E104", "Neha", 2)
)
print("Employees with 4 or more days present:")
for emp_id, name, days in attendance:
    if days >= 4:
        print(name)

count_less_than_4 = 0
for emp_id, name, days in attendance:
    if days < 4:
        count_less_than_4 += 1
print(f"\nNumber of employees present less than 4 days: {count_less_than_4}")

max_days = 0
max_name = ""
for emp_id, name, days in attendance:
    if days > max_days:
        max_days = days
        max_name = name

print(f"\nEmployee with highest attendance: {max_name} ({max_days} days)")

#sample output
# Employees with 4 or more days present:
# John
# Amit

# Number of employees present less than 4 days: 2

# Employee with highest attendance: John (5 days)
# PS C:\Users\303464\Desktop\Training> 
