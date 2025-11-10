# TASK 4 - Calculate age groups

age = int(input("Enter the age: "))
level = lambda age: ("Junior" if age <30  else "Mid level" if  age < 45 else "Senior" )
print(level(age))

# Sample Output
# Enter the age: 40
# Mid level
