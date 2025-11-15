# Lambda function to calculate salary after 10% increment
func = lambda salary: (salary + salary * 0.10)
sal = func(10000)
print("The salary is", sal)

# List of employee IDs
ids = [101, 102, 103, 104, 105, 106]

# Filter even IDs using lambda function
res = list(filter(lambda a: a % 2 == 0, ids))
print("Filtered value is ", res)

# List of employees with their performance scores
employees = [("Deva", 3), ("Prasath", 7), ("Raj", 2), ("Gokul", 5)]

# Sort employees based on their performance score using lambda function
employees.sort(key=lambda x: x[1])
print("Sorted Employees is ", employees)

# Input age
age = int(input())

# Lambda function to determine the designation based on age
func = lambda x: "Junior" if age < 30 else "Mid-level" if age >= 30 and age < 45 else "Senior"
res = func(age)
print("Designation is ", res)

# Lists of names and departments
names = ["Dev", "Raj", "Prasath", "Gokul"]
dept = ["It", "Cse", "Aiml", "Ise"]

# Format and combine names and departments using lambda and map
res = list(map(lambda a, b: f"{a} works in {b}", names, dept))
print("Formatted result is ", res)



##Sample output

# The salary is 11000.0
# Filtered value is  [102, 104, 106]
# Sorted Employees is  [('Raj', 2), ('Deva', 3), ('Gokul', 5), ('Prasath', 7)]
# 50
# Designation is  Senior
# Formatted result is  ['Dev works in It', 'Raj works in Cse', 'Prasath works in Aiml', 'Gokul works in Ise']