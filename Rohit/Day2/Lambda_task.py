# Step 1: Calculate 10% bonus on each salary
salaries = [40000, 50000, 60000, 70000, 80000]
bonus = list(map(lambda sal: sal + sal * 0.1, salaries))  # Apply 10% bonus
print(salaries)  # Original salaries list

# Output:
# [40000, 50000, 60000, 70000, 80000]


# Step 2: Filter even IDs from the list
filterId = [12, 7, 8, 75, 43, 22, 68, 49]
ans = list(filter(lambda id: id % 2 == 0, filterId))  # Keep only even IDs
print(ans)

# Output:
# [12, 8, 22, 68]


# Step 3: Sort employees by their experience (second element in tuple)
employees = [("Rahul ", 3), ("Priya", 7), ("Karan", 2), ("Divya", 4)]
employees.sort(key=lambda x: x[1])  # Sort by experience
print(employees)

# Output:
# [('Karan', 2), ('Rahul ', 3), ('Divya', 4), ('Priya', 7)]


# Step 4: Determine overtime status based on age
overtime_status = lambda age: "Junior-level" if age < 30 else ("mid-level" if age > 30 or age < 45 else "Senior-level")
print(overtime_status(36))  # Age = 36

# Output:
# mid-level


# Step 5: Merge names and departments into formatted strings
names = ['Arun', 'Neha', 'Vikram']
depts = ['HR', 'IT', 'FINANCE']
merged = list(map(lambda x: f"{x[0]} works in {x[1]}", zip(names, depts)))  # Combine name and department
print(merged)

# =============Sample Output==================:
#[40000, 50000, 60000, 70000, 80000]
# [12, 8, 22, 68]
# [('Karan', 2), ('Rahul ', 3), ('Divya', 4), ('Priya', 7)]
# mid-level
# ['Arun works in HR', 'Neha works in IT', 'Vikram works in FINANCE']