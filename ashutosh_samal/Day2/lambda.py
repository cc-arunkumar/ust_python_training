# List of employees with their names and salaries
employees = [("pooja", 35000), ("Ravi", 15000), ("Amit", 20000)]

# Sorting the list of employees by their salaries (second item in the tuple)
employees.sort(key=lambda x: x[1])
# Print the sorted list of employees
print(employees)

# Lambda function to check overtime status based on working hours
overtime_status = lambda hours: "Overtime" if hours > 8 else "Regular"
# Check if 8 hours is considered overtime or regular
print(overtime_status(8))

# List of salaries
salaries = [40, 50, 60, 70, 80]

# Using map to calculate the bonus (50% of each salary)
bonus = list(map(lambda sal: sal * 0.5, salaries))
# Print the list of bonuses
print(bonus)

# Filtering the salaries list to find those greater than 50
filt = list(filter(lambda sal: sal > 50, salaries))
# Print the filtered list of salaries (greater than 50)
print(filt)

# Importing reduce from functools to apply a rolling calculation (summing all elements)
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce to calculate the sum of all elements in the list
result = reduce(lambda a, b: a + b, numbers)
# Print the total sum
print(result)
