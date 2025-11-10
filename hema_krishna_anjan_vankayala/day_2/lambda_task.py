#Task 1: Calculate Bonus for Employees
# Your team’s HR automation system needs to quickly calculate a 10% bonus for each employee based on their monthly salary.

# Requirement:
# Write a lambda function that takes a salary as input and returns the salary + 10% bonus.

# Example Input:
# salary = 50000

# Expected Output:
# 55000.0

# (Hint: bonus = salary * 0.10)

salary = int(input("Enter the Salary Amount: "))
salary_with_bonus = lambda salary: salary + (salary * 0.1)
print(f"Total Salary including Bonus is: Rs.{salary_with_bonus(salary)}")

#Task 2: Identify Even Numbers in a List

# You have a list of employee IDs, and you need to filter out only even IDs for an internal audit.

# Requirement:
# Use a lambda function with the filter() method to select even IDs.

# Example Input:
# ids = [101, 102, 103, 104, 105, 106]

# Expected Output:
# [102, 104, 106]

ids = list(map(int, input("Enter Employee IDs: ").split()))
even_numbers_list = list(filter(lambda x: x%2==0,ids))
print(even_numbers_list)

#Task 3: Sort Employees by Experience
# You have a list of employees with their years of experience, and you need to sort them by experience in ascending order.

# Requirement:
# Use a lambda function as a sorting key.

# Example Input:

# employees = [
#     ("Rahul", 3),
#     ("Priya", 7),
#     ("Karan", 2),
#     ("Divya", 5)
# ]


# Expected Output:
# [('Karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]

employees=[("pooja",5),("hemanth",3),("yogesh",7),("sneha",2),("rahul",4)]
sorted_employees = sorted(employees, key=lambda x: x[1])
print(sorted_employees)

#Task 4: Categorize Age Groups

# HR wants to classify employees as:
# “Junior” → if age < 30
# “Mid-level” → if 30 ≤ age < 45
# “Senior” → if age ≥ 45
# Use a lambda with conditional expressions.

# Example Input:
# age = 35

# Expected Output:
# "Mid-level"

age = int(input("Enter the Age: "))
classify_age = lambda age: "Junior" if age>30 else "Mid-level" if age<=30 and age>45 else "Senior"
print(classify_age(age))

#Task 5: Combine Two Lists (Employee and Department)

# You have two lists — one with employee names and another with their departments.
# Use a lambda to merge them into a single formatted string.

# Example Input:
# names = ['Arun', 'Neha', 'Vikram']
# depts = ['HR', 'IT', 'Finance']


# Expected Output:
# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']

names = input("Enter Employee Names: ").split()
departments = input("Enter Departments: ").split()
combined_list = list(map(lambda name,department: f"{name} works in {department}",names,departments))
print(combined_list)
