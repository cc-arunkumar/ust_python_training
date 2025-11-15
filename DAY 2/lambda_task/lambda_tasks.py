"""
Task 1: Calculate Bonus for Employees

Your team’s HR automation system needs to quickly calculate a 10% bonus for each employee based on their monthly salary.

Requirement:
Write a lambda function that takes a salary as input and returns the salary + 10% bonus.
"""

print("Calculate Bonus for Employees")
bonus_for_employees= lambda salary: salary+salary*0.1   # Lambda to calculate salary + 10% bonus
print(bonus_for_employees(5000))   # Test the lambda with a salary of 5000


"""
Task 2: Identify Even Numbers in a List

You have a list of employee IDs, and you need to filter out only even IDs for an internal audit.

Requirement:
Use a lambda function with the filter() method to select even IDs.

"""

employee_ids=[101,102,103,104,105,106]
even_ids=list(filter(lambda id : id%2==0,employee_ids))   # Filter employee IDs that are even
print(even_ids)   # Print the filtered list


"""
You have a list of employees with their years of experience, and you need to sort them by experience in ascending order.

Requirement:
Use a lambda function as a sorting key.

"""


employees=[
    ("Rahul",3),
    ("Priya",7),
    ("Karan",2),
    ("Divya",5)
]

employees.sort(key=lambda x:x[1])   # Sort employees by years of experience (second element)
print(employees)   # Print sorted list


"""
Task 4: Categorize Age Groups

HR wants to classify employees as:

“Junior” → if age < 30

“Mid-level” → if 30 ≤ age < 45

“Senior” → if age ≥ 45

Use a lambda with conditional expressions.

"""

age=int(input("Enter Your Age: "))   # Input age
designation=lambda a: "Junior" if a < 30 else "Mid-Level" if a <= 45 else "Senior"   # Lambda to classify age
print(designation(age))   # Print the classification



"""
Combine Two Lists (Employee and Department)

You have two lists — one with employee names and another with their departments.
Use a lambda to merge them into a single formatted string.
"""

names=["Ajth","Gowtham","Virat"]
departments=["Racing","Work","Sports"]

print(list(map(lambda name,dep : f"{name} works in {dep} department",names,departments)))   # Merge lists using map + lambda


"""
SAMPLE OUTPUT

5500.0
[102, 104, 106]
[('Karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]
Enter Your Age: 21
Junior
['Ajth works in Racing department', 'Gowtham works in Work department', 'Virat works in Sports department']
"""
