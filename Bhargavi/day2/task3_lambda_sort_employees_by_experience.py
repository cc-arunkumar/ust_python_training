#Sort Employees by Experience
# Task 3: Sort Employees by Experience
# You have a list of employees with their years of experience, and you need to sort them by experience in ascending order.
# Requirement:
# Use a lambda function as a sorting key.
# Example Input:
# employees = [("Rahul", 3),("Priya", 7),("Karan", 2),("Divya", 5)]


# List of employees with tasks completed (name, tasks)
employees = [("Meena", 3), ("Vani", 7), ("Sri", 2), ("bhanu", 5)]

# Sort employees based on number of tasks (x[1] refers to tasks)
sorted_employees = sorted(employees, key=lambda x: x[1])

# Print sorted list
print(sorted_employees)


#  Output:
# [('Sri', 2), ('Meena', 3), ('bhanu', 5), ('Vani', 7)]
